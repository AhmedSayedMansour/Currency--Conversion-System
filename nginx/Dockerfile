FROM nginx:1.25.1-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/nginx.conf

COPY /build /usr/share/nginx/html

# When the container starts, replace the env.js with values from environment variables
CMD ["/bin/sh",  "-c",  "envsubst < /usr/share/nginx/html/assets/env.sample.js > /usr/share/nginx/html/assets/env.js && exec nginx -g 'daemon off;'"]


RUN cat /etc/nginx/conf.d/nginx.conf \
    && mkdir -p /opt/application/webapp/staticfiles \
    && ls -al /opt/application/webapp/staticfiles