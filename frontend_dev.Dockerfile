# base image
FROM node:13.8.0-alpine as build

# set working directory
WORKDIR /frontend

# add `/app/node_modules/.bin` to $PATH
ENV PATH /frontend/node_modules/.bin:$PATH

# install and cache app dependencies
RUN yarn global add react-scripts@3.4.0

COPY frontend/package.json ./package.json
RUN yarn install
COPY frontend/  ./
RUN yarn run build

COPY start.sh /opt/start_frontend.sh
RUN chmod +x /opt/start_frontend.sh