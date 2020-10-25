#FROM node:13.7.0-alpine
#
#RUN npm install -g http-server
#
#WORKDIR /app
#
#COPY package*.json ./
#
#RUN npm install
#
#COPY prod_nginx.conf /etc/nginx/nginx.confg
#COPY . .
#
#RUN ROOT_API=http://localhost:5001 npm run build
#
#EXPOSE 8080
#
#CMD [ "http-server", "dist" ]

# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY ./.nginx/nginx.conf /etc/nginx/nginx.conf

## Remove default nginx index page
RUN rm -rf /usr/share/nginx/html/*

COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
