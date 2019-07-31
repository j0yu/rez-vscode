FROM centos

RUN yum -y install git make gcc ncurses-devel gettext-devel ruby perl # gpm-devel
# RUN yum -y install vim

ARG VERSION
ARG INSTALL_DIR

RUN mkdir -vp ${INSTALL_DIR}
RUN git clone \
        https://github.com/vim/vim.git \
        /usr/local/src/vim
WORKDIR /usr/local/src/vim/src
RUN git checkout v${VERSION}

# RUN ./configure --enable-perlinterp=dynamic --enable-pythoninterp=dynamic --enable-rubyinterp=dynamic
RUN ./configure --prefix=${INSTALL_DIR} -q
RUN make -j$(nproc)
CMD make install

# # Check how our vim compares (features) with the older one from yum/CentOS
# RUN make install
# RUN vim --version | sed -n -e '/):/,/:/ { s/  */\n/gp }' | grep '^+' | sort > /tmp/vim7.txt
# RUN ./vim --version | sed -n -e '/):/,/:/ { s/  */\n/gp }' | grep '^+' | sort > /tmp/vim8.txt
# RUN vimdiff /tmp/vim*
