set terminal wxt

set yrange [0:5]
set xrange [0:500]
set xlabel 'Minuten'
set ylabel 'Volt'

set xtic 100
set title "Akkumessungen bei 110Ohm Lastwiderstand (mit neuem HH frisch geladen)"
set key left bottom

plot '17-6-14.txt' using (($1-1402999940)/60):(($2/1024)*5) title 'Akku 67 = 0.250Ah' with lines lw 2
replot '17-6-14.txt' using (($1-1402999940)/60):(($3/1024)*5) title 'Akku 68 = 0.248Ah' with lines lw 2
replot '17-6-14.txt' using (($1-1402999940)/60):(($4/1024)*5) title 'Akku 69 = 0.244Ah' with lines lw 2
replot '17-6-14.txt' using (($1-1402999940)/60):(($5/1024)*5) title 'Akku 70 = 0.253Ah' with lines lw 2

# f(x)  = ((688/1024)*5)
f(x) = 3.359375
replot f(x) title '3.3V'  lw 2

# f(x)  = ((475/1024)*5)
a(x) = 2.3193359375
replot a(x) title 'Abschaltung 2.32V'  lw 2

set terminal pdf
set output "akku - 17-06-14.pdf"
replot


