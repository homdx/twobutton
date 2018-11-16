FROM homdx/kivymd-store:003-36

COPY . ${HOME_DIR}/testapp

RUN sudo chown user ${HOME_DIR}/testapp -Rv

#USER root
#RUN chown user /home/user/ -R && chown -R user /home/user/hostcwd

#USER ${USER}

#Add after RUN sudo chown user ${WORK_DIR}/app2 -Rv
ARG KIVYMDSTORE_VERSION=0.0.2
ARG KIVYMDSTORE_HASH=b80303c87d20f088531e6fbdc050550bb4c0ebaa0f5c6b665a98569884f6156b

RUN cd ${HOME_DIR}/testapp && set -ex \
&& wget https://github.com/homdx/twobutton/releases/download/${KIVYMDSTORE_VERSION}/dot-buildozer.tar.gz \
&& echo "${KIVYMDSTORE_HASH}  dot-buildozer.tar.gz" | echo sha256sum -c \
&& tar -xf dot-buildozer.tar.gz && rm dot-buildozer.tar.gz \
&& echo '-----Python 3 ----' && cd ${HOME_DIR}/testapp && time buildozer android debug || echo "Fix build apk" \
&& sudo cp -v ${HOME_DIR}/testapp/.buildozer/android/platform/build/dists/twobutton/bin/Twobutton*debug.apk ${WORK_DIR}

CMD tail -f /var/log/faillog

#ENTRYPOINT ["buildozer"]
