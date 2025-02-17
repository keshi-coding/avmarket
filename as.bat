@echo off
echo [🛠️] Atualizando arquivos estáticos...
docker-compose exec web bash -c "rm -rf /app/staticfiles && python manage.py collectstatic --noinput"
echo [✅] Atualização concluída!
pause
