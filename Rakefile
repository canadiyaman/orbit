namespace :setup do
  desc "Orbit installation has started"
  task :start do
    system %{
      pip install -r requirements.txt
      createdb -E UTF8 -T template0 --lc-collate=tr_TR.UTF-8 --lc-ctype=tr_TR.UTF-8 orbit &&
      python manage.py migrate &&
      python manage.py createapiuser -username default &&
      python manage.py loadinitialdata -c 500 -cn Work,Holiday,Gym,Family
      echo "the installation ended..."
    }
  end
end