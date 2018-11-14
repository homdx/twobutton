FROM homdx/kivymd-store:003-36

COPY . ${HOME_DIR}/testapp

RUN sudo chown user ${HOME_DIR}/testapp -Rv

#USER root
#RUN chown user /home/user/ -R && chown -R user /home/user/hostcwd

#USER ${USER}

RUN echo '-----Python 3 ----' && cd ${HOME_DIR}/testapp && time buildozer android debug || echo "Fix build apk" \
&& sudo cp -v ${HOME_DIR}/testapp/.buildozer/android/platform/build/dists/twobutton/bin/Twobutton-0.1-debug.apk ${WORK_DIR}

CMD tail -f /var/log/faillog

#ENTRYPOINT ["buildozer"]
