# production environment
FROM nginx:alpine
COPY --from=docker.magical.rocks/dev-website:latest /mainpage/build /usr/share/nginx/html
COPY --from=docker.magical.rocks/dev-website:latest /opt/start.sh /opt/start_frontend.sh
EXPOSE 80

# start app
CMD ["/opt/start.sh"]