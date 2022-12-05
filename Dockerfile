FROM pretix/standalone:stable
USER root
COPY . ./email_plugin
RUN cd ./email_plugin
RUN python setup.py develop
RUN make
RUN cd ../
USER pretixuser
RUN cd /pretix/src && make production
