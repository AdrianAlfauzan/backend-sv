📁 Backend README
D:\backend-sv\README.md
markdown

# Backend - Sharing Vision 2023 (Microservices)

Backend untuk aplikasi Sharing Vision menggunakan arsitektur **microservices** dengan **Docker**.

## 🚀 Teknologi

| Komponen            | Teknologi         |
| ------------------- | ----------------- |
| **API Gateway**     | Node.js + Express |
| **Article Service** | Python + FastAPI  |
| **Database**        | MySQL 8.0         |
| **Orchestration**   | Docker Compose    |

---

## 📁 Struktur Folder

backend-sv/
├── api-gateway/ # API Gateway (Node.js)
│ ├── src/
│ │ └── index.js
│ ├── package.json
│ ├── Dockerfile
│ └── .env
│
├── article-service/ # Article Service (Python)
│ ├── app/
│ │ ├── main.py
│ │ ├── models.py
│ │ ├── schemas.py
│ │ ├── crud.py
│ │ ├── database.py
│ │ └── config.py
│ ├── requirements.txt
│ ├── Dockerfile
│ └── .env
│
├── docker-compose.yml
└── .env

text

---

## ⚙️ Prasyarat

- **Docker Desktop** terinstall dan berjalan
- **Git** (opsional)
- **Port tersedia**: 3306, 8001, 8080

---

## 🚀 Cara Menjalankan

### 1. Clone / Buka Folder Project

```bash
cd D:\backend-sv
2. Jalankan Docker Compose
bash
docker-compose up -d
Proses ini akan:

Download image MySQL 8.0

Build image Article Service (Python)

Build image API Gateway (Node.js)

Menjalankan semua container

3. Cek Status Container
bash
docker ps
Harus muncul 3 container:

text
sharing-mysql              ✅ Up (healthy)
sharing-article-service    ✅ Up
sharing-api-gateway        ✅ Up
4. Buat Tabel Database (Pertama Kali Saja)
bash
docker exec -it sharing-mysql mysql -uapp_user -papp_password article_db -e "
CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(200) NOT NULL,
    Content TEXT NOT NULL,
    Category VARCHAR(100) NOT NULL,
    Status VARCHAR(100) DEFAULT 'Draft',
    Created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
"
5. Tambahkan Data Dummy (Opsional)
bash
docker exec -it sharing-mysql mysql -uapp_user -papp_password article_db -e "
INSERT INTO posts (Title, Content, Category, Status) VALUES
('Belajar Microservices dengan Docker', 'Microservices adalah arsitektur yang memecah aplikasi menjadi layanan-layanan kecil yang independen. Dengan Docker, kita bisa menjalankan setiap service dalam container yang terisolasi.', 'DevOps', 'Publish'),
('Panduan Next.js 14 untuk Pemula', 'Next.js 14 hadir dengan berbagai fitur baru seperti Server Components dan App Router. Artikel ini akan memandu Anda memulai dengan Next.js.', 'Frontend', 'Publish');
"
🌐 Akses API
Service	URL
API Gateway	http://localhost:8080
Article Service (Health)	http://localhost:8001/health
Swagger UI	http://localhost:8080/docs
Get Articles	http://localhost:8080/article/10/0
📋 Endpoint API
Method	URL	Deskripsi
POST	/article	Buat artikel baru
GET	/article/{limit}/{offset}	Lihat semua artikel (paging)
GET	/article/{id}	Lihat artikel by ID
PATCH	/article/{id}	Update artikel
DELETE	/article/{id}	Hapus artikel
Contoh Request (POST)
json
{
  "title": "Belajar FastAPI dengan Docker",
  "content": "Ini adalah konten artikel dengan minimal 200 karakter. ",
  "category": "Programming",
  "status": "Publish"
}
🛑 Menghentikan Service
bash
docker-compose down
Untuk menghapus semua data (termasuk database):

bash
docker-compose down -v
🔧 Troubleshooting
Port 3306 sudah dipakai
Matikan XAMPP MySQL atau ubah port di docker-compose.yml:

yaml
ports:
  - "3307:3306"  # Ganti 3306:3306
Tabel tidak ditemukan
Jalankan perintah CREATE TABLE di atas.

Container tidak mau jalan
bash
docker-compose logs article-service --tail 50
📦 Build Ulang (Jika Ada Perubahan Kode)
bash
docker-compose build --no-cache
docker-compose up -d
📝 Catatan
Database di dalam Docker menggunakan MySQL 8.0 dengan autentikasi mysql_native_password

Kredensial default: app_user / app_password

Database name: article_db

Selesai! Backend siap digunakan. 🚀
```
