const express = require("express");
const { createProxyMiddleware } = require("http-proxy-middleware");
const cors = require("cors");
const morgan = require("morgan");
require("dotenv").config();

const app = express();
const PORT = process.env.PORT || 8080;

app.use(cors());
app.use(morgan("dev"));
app.use(express.json());

app.get("/health", (req, res) => {
  res.json({ status: "OK", service: "API Gateway", timestamp: new Date().toISOString() });
});

app.get("/", (req, res) => {
  res.json({
    message: "Sharing Vision API Gateway",
    service: "Article Service",
    endpoints: {
      "GET /health": "Health check",
      "GET /": "This page",
      "/article/*": "Article Service (Port 8001)",
      "/api/articles/*": "Article Service (Port 8001)",
    },
  });
});

app.use(
  "/article",
  createProxyMiddleware({
    target: process.env.ARTICLE_SERVICE_URL || "http://article-service:8001",
    changeOrigin: true,
    onProxyReq: (proxyReq, req) => {
      console.log(`[ARTICLE] ${req.method} ${req.url}`);
    },
    onError: (err, req, res) => {
      console.error("Article Service error:", err.message);
      res.status(503).json({ error: "Article service unavailable" });
    },
  }),
);

app.use(
  "/api/articles",
  createProxyMiddleware({
    target: process.env.ARTICLE_SERVICE_URL || "http://article-service:8001",
    changeOrigin: true,
    pathRewrite: { "^/api/articles": "" },
    onProxyReq: (proxyReq, req) => {
      console.log(`[ARTICLE] ${req.method} ${req.url}`);
    },
    onError: (err, req, res) => {
      console.error("Article Service error:", err.message);
      res.status(503).json({ error: "Article service unavailable" });
    },
  }),
);

app.listen(PORT, () => {
  console.log("API Gateway running on port", PORT);
  console.log("Article Service:", process.env.ARTICLE_SERVICE_URL || "http://article-service:8001");
  console.log("Routes: /article/* and /api/articles/*");
});
