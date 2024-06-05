FROM node:14

WORKDIR /app

COPY package.json /app/package.json
RUN npm install -g @vue/cli
RUN npm install

COPY . /app

RUN npm run build
#
#CMD ["npm", "run", "serve"]