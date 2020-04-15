# production environment
FROM nginx:alpine
COPY --from=[TODO]/dev-website:latest /mainpage/build /usr/share/nginx/html
COPY --from=[TODO]/dev-website:latest /opt/start.sh /opt/start_frontend.sh
EXPOSE 80

# start app
CMD ["/opt/start.sh"]