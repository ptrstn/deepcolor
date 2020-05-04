# base image
FROM node:13.8.0-alpine as build

# set working directory
WORKDIR /frontend

# add `/app/node_modules/.bin` to $PATH
ENV PATH /frontend/node_modules/.bin:$PATH

# install and cache app dependencies
RUN yarn global add react-scripts@3.4.0

COPY ./package.json ./package.json
RUN yarn install
COPY ./  ./
RUN yarn run build

COPY ./start_frontend.sh /opt/start.sh
RUN chmod +x /opt/start.sh

# production environment
FROM nginx:alpine
COPY --from=build /frontend/build /usr/share/nginx/html
COPY --from=build /opt/start.sh /opt/start.sh
EXPOSE 80

# start app
CMD ["/opt/start.sh"]