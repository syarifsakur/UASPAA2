# UAS_PAA2_SYARIF-MOHAMMAD-SYAKUR_F55121020
<h3>Nama : SYARIF MOHAMMAD SYAKUR</h3>
<h3>NIM  : F55121020</h3>
<h3>Kelas: A</h3>

<h5>Analisis Algoritma Bubble Sort dan Algoritma Insertion Sort:</h5>
Bubble Sort:

- Average Case: Pada kasus rata-rata, kompleksitas waktu Bubble Sort juga O(n^2), karena algoritma ini melakukan perbandingan dan pertukaran pada setiap pasangan elemen, terlepas dari kondisi awal array.
- Worst Case: Kasus terburuk terjadi ketika array dalam kondisi terbalik secara terurut atau acak dengan nilai yang tinggi (misalnya [99, 87, 90, ..., 1]). Pada kasus ini, Bubble Sort akan melakukan perbandingan dan pertukaran pada setiap pasangan elemen, sehingga kompleksitas waktu Bubble Sort adalah O(n^2), di mana n adalah jumlah elemen dalam array.
- Best Case: Kasus terbaik terjadi ketika array sudah dalam keadaan terurut secara menaik. Pada kasus ini, Bubble Sort hanya akan melakukan satu kali iterasi untuk memeriksa bahwa tidak ada pertukaran yang dilakukan, sehingga kompleksitas waktu Bubble Sort adalah O(n), di mana n adalah jumlah elemen dalam array.


Insertion Sort:

- Average Case: Pada kasus rata-rata, kompleksitas waktu Insertion Sort adalah O(n^2), karena algoritma ini melakukan pemindahan elemen-elemen yang diperlukan pada setiap iterasi, terlepas dari kondisi awal array.
- Worst Case: Kasus terburuk terjadi ketika array dalam kondisi terbalik secara terurut (misalnya [99, 95, 90, ..., 1]). Pada kasus ini, Insertion Sort harus memindahkan setiap elemen ke posisi yang benar dengan membandingkannya dengan elemen-elemen sebelumnya. Kompleksitas waktu Insertion Sort dalam kasus terburuk adalah O(n^2), di mana n adalah jumlah elemen dalam array.
- Best Case: Kasus terbaik terjadi ketika array sudah dalam keadaan terurut secara menaik. Pada kasus ini, Insertion Sort hanya akan memeriksa bahwa tidak ada pemindahan yang perlu dilakukan, sehingga kompleksitas waktu Insertion Sort adalah O(n), di mana n adalah jumlah elemen dalam array.


<h5>Analisis Algoritma TSP dan algoritma Djikstra:</h5>
Worst Case:

- Djikstra: Pada kasus terburuk, algoritma Djikstra akan mengunjungi setiap node dalam grafik dan memperbarui jarak terpendek untuk setiap node yang dikunjungi. Kompleksitas waktu algoritma Djikstra dalam kasus terburuk adalah O((V + E) log V), di mana V adalah jumlah node dan E adalah jumlah edge dalam grafik.
- TSP: Pada kasus terburuk, algoritma TSP akan mengunjungi setiap node secara berurutan sebanyak N - 1 kali, di mana N adalah jumlah total node dalam grafik. Oleh karena itu, kompleksitas waktu algoritma TSP dalam kasus terburuk adalah O(N^2).- Djikstra: Pada kasus terburuk, algoritma Djikstra akan mengunjungi setiap node dalam grafik dan memperbarui jarak terpendek untuk setiap node yang dikunjungi. Kompleksitas waktu algoritma Djikstra dalam kasus terburuk adalah O((V + E) log V), di mana V adalah jumlah node dan E adalah jumlah edge dalam grafik.

Best Case:

- Djikstra: Pada kasus terbaik, algoritma Djikstra mungkin memiliki simpul awal yang langsung terhubung ke semua simpul lain dengan jarak minimum. Dalam hal ini, algoritma hanya akan memperbarui jarak terpendek untuk setiap simpul yang dikunjungi, sehingga kompleksitas waktu algoritma Djikstra dalam kasus terbaik adalah O(V + E).
- TSP: Pada kasus terbaik, algoritma TSP mungkin memiliki simpul awal yang langsung terhubung ke simpul lain dengan jarak minimum. Dalam hal ini, algoritma hanya akan memilih simpul tersebut sebagai simpul berikutnya dalam setiap iterasi, sehingga kompleksitas waktu algoritma TSP dalam kasus terbaik adalah O(N).


Average Case:

- Djikstra: Untuk algoritma Djikstra, kompleksitas waktu rata-rata tergantung pada struktur grafik dan panjang edge-edge dalam grafik. Dalam kasus rata-rata, kompleksitas waktu algoritma Djikstra adalah sekitar O((V + E) log V), di mana V adalah jumlah node dan E adalah jumlah edge dalam grafik.
- TSP: Untuk algoritma TSP, kompleksitas waktu rata-rata tergantung pada struktur grafik dan jarak antara simpul-simpulnya. Dalam kasus rata-rata, algoritma TSP memiliki kompleksitas waktu sekitar O(N^2), di mana N adalah jumlah total node dalam grafik.

 
