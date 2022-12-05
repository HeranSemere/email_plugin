FROM pretix/standalone:stable
USER root
COPY . ./email_plugin
WORKDIR ./email_plugin
RUN python setup.py develop
RUN make
WORKDIR ../
USER pretixuser
RUN cd /pretix/src && make production
