FROM node:18 AS build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build
RUN npm prune --production


FROM node:18 AS run

ENV PORT=3000
ENV NODE_ENV=production

WORKDIR /app

RUN mkdir -p /app/build
COPY --from=build /app/build ./build
COPY --from=build /app/package.json ./package.json
COPY --from=build /app/node_modules ./node_modules

EXPOSE 3000

ENTRYPOINT ["node", "build"]
