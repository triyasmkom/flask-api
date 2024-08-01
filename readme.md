# Flusk API

## Local environment python

```bash
# install virtual env
pip install virtualenv

# Create virtual env
virtualenv env

# Activate virtual env
source env/bin/activate

# Deactivate virtual env
deactivate

# change versi pythone
virtualenv -p python3 env

```

## Install Package

```bash
# install flask
pip install flask

# install flask migrate
pip install flask-migrate

# install dot env
pip install python-dotenv

# install sql alchemy
pip install flask-sqlalchemy

# install driver mysql
pip install pymysql

pip install werkzeug

pip install flask-jwt-extended
```

## Migrate DB

```bash
# initial database
flask db init

# create migrate database
flask db migrate -m "membuat table user"

# upgrade database
flask db upgrade
```

## Menjalankan APP

```bash
# running mode development
flask run
```

## Deploy in Ubuntu Server

 1. Update dan Upgrade Sistem

    ```bash
    sudo apt update
    sudo apt upgrade
    ```

 2. Instalasi python

    ```bash
    sudo apt install python3

    sudo apt install python3-pip
    ```

 3. Membuat Virtual Environment

    ```bash
    sudo apt install python3-venv

    python3 -m venv myenv

    source myenv/bin/activate
    ```

 4. Menggunakan Python

    ```bash
    python3 script.py
    pip install nama_paket
    ```

    ```bash
    flask run
    pip install nama_paket
    ```

 5. Deaktivasi Virtual Environment

    ```bash
    deactivate
    ```

## Install Nginx in Ubuntu Server

 1. Instalasi Nginx

    ```bash
    sudo apt update
    sudo apt install nginx
    ```

 2. Mulai dan Aktifkan Nginx

    ```bash
    sudo systemctl start nginx
    sudo systemctl enable nginx
    ```

 3. Konfigurasi Firewall (Opsional)

    ```bash
    sudo ufw allow 'Nginx Full'
    ```

 4. Konfigurasi Server Block (Virtual Host)

    ```bash
    sudo nano /etc/nginx/sites-available/your_domain
    ```

    ```bash
    server {
        listen 80;
        server_name your_domain www.your_domain;

        location / {
            proxy_pass http://127.0.0.1:5000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    ```

 5. Mengaktifkan Konfigurasi Server Block

    ```bash
    sudo ln -s /etc/nginx/sites-available/your_domain /etc/nginx/sites-enabled/
    ```

 6. Periksa Konfigurasi Nginx

    ```bash
    sudo nginx -t
    ```

 7. Mulai Ulang Nginx

    ```bash
    sudo systemctl restart nginx
    ```

 8. Pengaturan DNS (Opsional)
    Jika Anda memiliki nama domain, pastikan untuk mengatur catatan DNS Anda untuk mengarah ke server Anda.

 9. Mengaktifkan HTTPS (Opsional)

    Instal Certbot dan plugin Nginx:

    ```bash
    sudo apt install certbot python3-certbot-nginx
    ```

    Dapatkan dan instal sertifikat SSL:

    ```bash
    sudo certbot --nginx -d your_domain -d www.your_domain
    ```

 10. Mengakses Situs Anda
    Setelah konfigurasi selesai, Anda harus dapat mengakses situs Anda melalui nama domain atau alamat IP yang dikonfigurasi.

## Menjalankan Flask dengan `nohup`

1. Menjalankan Flask dengan nohup

    ```bash
    nohup flask run --host=0.0.0.0 --port=5000 &
    ```

    - nohup memastikan proses tetap berjalan bahkan jika terminal ditutup.
    - host=0.0.0.0 mengizinkan akses ke server dari alamat IP mana pun.
    - port=5000 menentukan port yang akan digunakan (gantilah jika diperlukan).

    Output dari aplikasi akan disimpan di file nohup.out secara default.

2. Menjalankan Aplikasi Flask Otomatis Setelah Reboot
    Untuk memastikan aplikasi Flask dimulai secara otomatis setelah reboot, Anda dapat membuat service systemd untuk aplikasi Anda. Berikut adalah cara melakukannya:

    Buat file service baru di /etc/systemd/system/:

    ```bash
    sudo nano /etc/systemd/system/flaskapp.service
    ```

    Contoh Konfigurasi Service:

    ```bash
        [Unit]
    Description=Flask Application

    [Service]
    User=yourusername
    WorkingDirectory=/path/to/your/flaskapp
    Environment="PATH=/path/to/your/venv/bin"
    ExecStart=/path/to/your/venv/bin/flask run --host=0.0.0.0 --port=5000

    [Install]
    WantedBy=multi-user.target
    ```

    - User: Gantilah yourusername dengan nama pengguna Anda.
    - WorkingDirectory: Gantilah /path/to/your/flaskapp dengan jalur ke direktori aplikasi Flask Anda.
    - Environment: Gantilah /path/to/your/venv/bin dengan jalur ke direktori bin dalam lingkungan virtual Anda.
    - ExecStart: Gantilah /path/to/your/venv/bin/flask dengan jalur ke skrip Flask dalam lingkungan virtual Anda.

    Reload Systemd dan Mulai Service

    ```bash
    # Reload systemd untuk mengenali service baru:
    sudo systemctl daemon-reload

    # Mulai service Flask Anda:
    sudo systemctl start flaskapp

    # Pastikan service berjalan dengan benar:
    sudo systemctl status flaskapp

    # Mengaktifkan Service Otomatis Saat Boot
    sudo systemctl enable flaskapp
    ```

Ref: [Link](https://www.youtube.com/watch?v=9kjhBjNvVYw&list=PLH1gH0TmFBBhqlfb9f12nb0V8VXaGJGNI&index=4)