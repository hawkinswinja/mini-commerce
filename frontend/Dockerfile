# Stage 1: Build the React Vite app
FROM node:20.14-alpine3.20  AS build

WORKDIR /app

COPY package.json package-lock.json /app/
RUN npm ci

COPY . .
RUN npm run build

# Stage 2: Serve the app with NGINX
FROM nginx:alpine3.20-slim AS production

COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]