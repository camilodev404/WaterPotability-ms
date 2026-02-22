#!/usr/bin/env bash
set -euo pipefail

API_DIR=/home/ubuntu/WaterPotability-ms
DASH_DIR=/home/ubuntu/WaterPotability-dashboard

sudo apt update
sudo apt install -y python3-venv python3-pip nginx nodejs npm

cd "$API_DIR"
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

sudo cp deploy/systemd/waterpotability-api.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now waterpotability-api

cd "$DASH_DIR"
npm install
npm run build

sudo mkdir -p /var/www/waterpotability-dashboard
sudo cp -r dist/waterpotability-dashboard/browser/* /var/www/waterpotability-dashboard/

sudo cp "$API_DIR"/deploy/nginx/waterpotability.conf /etc/nginx/sites-available/waterpotability
sudo ln -sf /etc/nginx/sites-available/waterpotability /etc/nginx/sites-enabled/waterpotability
sudo nginx -t
sudo systemctl restart nginx

echo "Deployment completed"
