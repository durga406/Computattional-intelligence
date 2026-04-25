;; Rectangle
(defun area-rectangle (length width)
  (* length width))

(defun perimeter-rectangle (length width)
  (* 2 (+ length width)))


;; Square
(defun area-square (side)
  (* side side))

(defun perimeter-square (side)
  (* 4 side))


;; Circle
(defun area-circle (radius)
  (* 3.14 radius radius))

(defun perimeter-circle (radius)
  (* 2 3.14 radius))


CL-USER 1 > (area-rectangle 5 3)
15

CL-USER 2 > (area-square 5)
25

CL-USER 3 > (area-circle 2)
12.56

CL-USER 4 > (perimeter-rectangle 5 3)
16

CL-USER 5 > (perimeter-square 5)
20

CL-USER 6 > (perimeter-circle 2)
12.56

CL-USER 7 > (perimeter-circle 4)
25.12
-------string operetion-------
;; Concatenation
(defun concat-strings (s1 s2)
  (concatenate 'string s1 s2))

;; Length
(defun string-length-fn (s)
  (length s))

;; Uppercase
(defun to-uppercase (s)
  (string-upcase s))

(concat-strings "Hello" "world")
"Helloworld"

CL-USER 9 > (string-length-fn "MepcoSchlenkEngg")
16

CL-USER 10 > (to-uppercase "mepco_schlenk_engg")
"MEPCO_SCHLENK_ENGG"

--------calculator-----
(defun calculator ()
  (format t "Enter first number: ")
  (setq a (read))

  (format t "Enter operator (+, -, *, /): ")
  (setq op (read))

  (format t "Enter second number: ")
  (setq b (read))

  (cond
    ((eq op '+) (format t "Result: ~a" (+ a b)))
    ((eq op '-) (format t "Result: ~a" (- a b)))
    ((eq op '*) (format t "Result: ~a" (* a b)))
    ((eq op '/) (format t "Result: ~a" (/ a b)))
    (t (format t "Invalid operator"))))


