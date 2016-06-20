FROM ubuntu:16.04

RUN apt update && apt upgrade -y && apt install -y nginx ca-certificates curl bzip2
RUN locale-gen en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

EXPOSE 80
EXPOSE 443

RUN curl https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
  -o miniconda.sh \
  && bash miniconda.sh -b -p /opt/miniconda/ \
  && echo 'export PATH=/opt/miniconda/bin:$PATH' > /etc/profile.d/conda.sh

ENV PATH /opt/miniconda/bin:$PATH

RUN conda install -y -q flask pandas pymongo \
  && conda install -y -q -c conda-forge uwsgi \
  && pip install flask_restful flask_json flask_httpauth

RUN rm /etc/nginx/sites-enabled/default \
  && mkdir /var/log/uwsgi && chown -R www-data:www-data /var/log/uwsgi \
  && mkdir /var/www/auxservice-www && chown -R www-data:www-data /var/www/auxservice-www \
  && ln -s /var/www/auxservice-www/auxservice_nginx.conf /etc/nginx/conf.d/


COPY auxservice_nginx.conf /var/www/auxservice-www/
COPY auxservice /var/www/auxservice-www/auxservice
COPY auxservice_uwsgi.ini /var/www/auxservice-www/
COPY run.py /var/www/auxservice-www/
RUN chown -R www-data:www-data /var/www/auxservice-www


COPY start.sh .
CMD bash start.sh
