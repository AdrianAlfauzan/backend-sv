## ✅ README Backend yang Lengkap dengan Instalasi Node Modules

Karena `node_modules` tidak di-upload ke Git (sudah di-.gitignore), maka **orang yang clone project harus install sendiri**.

---

## 📁 Backend README

### `D:\backend-sv\README.md`

```markdown
# Backend - Sharing Vision 2023 (Microservices)

Backend Sharing Vision dengan arsitektur microservices menggunakan Docker.

---

## 🚀 Teknologi

| Komponen            | Teknologi         |
| ------------------- | ----------------- |
| **API Gateway**     | Node.js + Express |
| **Article Service** | Python + FastAPI  |
| **Database**        | MySQL 8.0         |
| **Orchestration**   | Docker Compose    |

---

## 📁 Struktur Folder
```

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
├── .gitignore
└── README.md

````

---

## ⚙️ Prasyarat

- **Docker Desktop** terinstall dan berjalan
- **Git** (untuk clone)
- Port **3306**, **8001**, **8080** tersedia

---

## 🚀 Cara Menjalankan

### 1. Clone Repository

```bash
git clone <repository-url>
cd backend-sv
````

### 2. Install Dependencies API Gateway

> ⚠️ `node_modules` tidak di-upload ke Git, jadi harus install sendiri!

```bash
cd api-gateway
npm install
cd ..
```

### 3. Jalankan Docker Compose

```bash
docker-compose up -d
```

Docker akan:

- Download image MySQL 8.0
- Build image Article Service (Python)
- Build image API Gateway (Node.js)
- Menjalankan semua container

### 4. Cek Status Container

```bash
docker ps
```

Harus muncul 3 container:

```
sharing-mysql              ✅ Up (healthy)
sharing-article-service    ✅ Up
sharing-api-gateway        ✅ Up
```

### 5. Buat Tabel Database (Pertama Kali Saja)

```bash
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
```

### 6. Tambahkan Data Dummy (Opsional)

```bash
docker exec -it sharing-mysql mysql -uapp_user -papp_password article_db -e "
INSERT INTO posts (Title, Content, Category, Status) VALUES
('Belajar Microservices dengan Docker', 'Microservices adalah arsitektur yang memecah aplikasi menjadi layanan-layanan kecil yang independen. Dengan Docker, kita bisa menjalankan setiap service dalam container yang terisolasi.', 'DevOps', 'Publish'),
('Panduan Next.js 14 untuk Pemula', 'Next.js 14 hadir dengan berbagai fitur baru seperti Server Components dan App Router.', 'Frontend', 'Publish');
"
```

---

## 🌐 Akses API

| Service          | URL                                  |
| ---------------- | ------------------------------------ |
| **API Gateway**  | `http://localhost:8080`              |
| **Health Check** | `http://localhost:8001/health`       |
| **Swagger UI**   | `http://localhost:8080/docs`         |
| **Get Articles** | `http://localhost:8080/article/10/0` |

---

## 📋 Endpoint API

| Method | URL                         | Deskripsi                    |
| ------ | --------------------------- | ---------------------------- |
| POST   | `/article`                  | Buat artikel baru            |
| GET    | `/article/{limit}/{offset}` | Lihat semua artikel (paging) |
| GET    | `/article/{id}`             | Lihat artikel by ID          |
| PATCH  | `/article/{id}`             | Update artikel               |
| DELETE | `/article/{id}`             | Hapus artikel                |

### Contoh Request (POST)

```json
{
  "title": "Belajar FastAPI dengan Docker",
  "content": "Ini adalah konten artikel dengan minimal 200 karakter. Ini adalah konten artikel dengan minimal 200 karakter. Ini adalah konten artikel dengan minimal 200 karakter. Ini adalah konten artikel dengan minimal 200 karakter. Ini adalah konten artikel dengan minimal 200 karakter. Ini adalah konten artikel dengan minimal 200 karakter.",
  "category": "Programming",
  "status": "Publish"
}
```

### Contoh Response (GET /article/10/0)

```json
[
  {
    "id": 1,
    "title": "Belajar Microservices dengan Docker",
    "content": "Microservices adalah arsitektur yang memecah aplikasi menjadi layanan-layanan kecil yang independen.",
    "category": "DevOps",
    "status": "Publish",
    "created_date": "2026-08-08T12:00:00",
    "updated_date": "2026-08-08T12:00:00"
  }
]
```

### Validasi Request

| Field      | Validasi                                |
| ---------- | --------------------------------------- |
| `title`    | Required, min 20 karakter               |
| `content`  | Required, min 200 karakter              |
| `category` | Required, min 3 karakter                |
| `status`   | Harus `Publish`, `Draft`, atau `Thrash` |

---

## 🛑 Stop Service

```bash
docker-compose down
```

Hapus semua data (termasuk database):

```bash
docker-compose down -v
```

---

## 🔧 Troubleshooting

### Port 3306 sudah dipakai

Matikan XAMPP MySQL atau ubah port di `docker-compose.yml`:

```yaml
ports:
  - "3307:3306" # Ganti 3306:3306
```

### Tabel tidak ditemukan

Jalankan perintah CREATE TABLE di atas.

### Lihat error logs

```bash
docker-compose logs article-service --tail 50
docker-compose logs api-gateway --tail 50
```

### Build ulang setelah ada perubahan kode

```bash
docker-compose build --no-cache
docker-compose up -d
```

---

## 📦 Dependencies

### API Gateway (Node.js)

```bash
cd api-gateway
npm install
```

Dependencies:

- `express`
- `http-proxy-middleware`
- `cors`
- `dotenv`
- `morgan`
- `nodemon` (dev)

### Article Service (Python)

Dependencies otomatis terinstall saat Docker build dari `requirements.txt`:

- `fastapi`
- `uvicorn`
- `sqlalchemy`
- `pymysql`
- `python-dotenv`
- `pydantic`

---

## 📝 Catatan

- Database di dalam Docker menggunakan **MySQL 8.0**
- Kredensial default: `app_user` / `app_password`
- Database name: `article_db`
- `node_modules` tidak di-upload ke Git (sudah di `.gitignore`)

---

**Selesai! Backend siap digunakan.** 🚀

```

---

## 📋 Ringkasan untuk Penilai

| Step | Perintah |
|------|----------|
| **1. Clone** | `git clone <url>` |
| **2. Install Node Modules** | `cd api-gateway && npm install` |
| **3. Jalankan Docker** | `docker-compose up -d` |
| **4. Buat Tabel** | Jalankan query SQL di atas |
| **5. Akses API** | `http://localhost:8080` |

---

**Sekarang README sudah lengkap dengan instruksi install node_modules!** 🚀
```
