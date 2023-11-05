FROM python:3.11-slim-bullseye as builder

LABEL name="DROP" \
    description="Base Project" \
    version="1.0.0"

ENV APP_HOME=/opt/application/webapp
WORKDIR $APP_HOME
# See in .dockerignore to ignore files in COPY
COPY ./pyproject.toml $APP_HOME

# libmariadb-dev-compat         mariadb requirement
RUN apt-get update
RUN apt-get install --yes --no-install-recommends gcc netcat libmariadb-dev-compat curl libstdc++6 apt-transport-https ca-certificates
RUN update-ca-certificates
RUN pip install --no-color --no-warn-script-location --no-cache-dir poetry
RUN poetry config virtualenvs.create true
RUN poetry config virtualenvs.in-project true
RUN poetry add mysqlclient@2.1.1 gunicorn
RUN poetry install --extras mysql
#RUN useradd -m -r user
#RUN chown -R user $APP_HOME
RUN apt-get autoremove --yes --allow-remove-essential --purge gcc openssl login passwd gzip
COPY . $APP_HOME
RUN chmod +x $APP_HOME/docker-entrypoint.sh
RUN find .venv -regex '.*\(/tests.*/\|/test.*/\|/*.pyc\|/*.dist-info\|/__pycache__\|/slapdtest\)$' -exec rm -rf "{}" +
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/log/* /var/cache/*
RUN rm -rf /root/* /root/.cache /root/.local

#USER user

EXPOSE 8000
ENTRYPOINT ["/bin/sh", "/opt/application/webapp/docker-entrypoint.sh"]
