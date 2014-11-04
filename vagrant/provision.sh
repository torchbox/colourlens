apt-get update -y
apt-get install -y build-essential python-setuptools python-dev git
apt-get install -y libjpeg-dev libtiff-dev zlib1g-dev libfreetype6-dev liblcms2-dev
apt-get install -y postgresql libpq-dev


# Database setup
su - postgres -c "createuser -s vagrant"
su - vagrant -c "createdb colourlens"


# Virtualenv setup
easy_install pip
pip install virtualenv

su - vagrant -c "virtualenv /home/vagrant/venv"
su - vagrant -c "/home/vagrant/venv/bin/pip install -r /vagrant/requirements.txt"
su - vagrant -c "/home/vagrant/venv/bin/python /vagrant/manage.py migrate --noinput"


cp -p /vagrant/vagrant/bashrc /home/vagrant/.bashrc
