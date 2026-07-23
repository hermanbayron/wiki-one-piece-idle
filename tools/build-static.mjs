import { cp, mkdir, rm, writeFile } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";

const root = process.cwd();
const dist = path.join(root, "dist");

const entries = [
  ".openai",
  "assets",
  "data",
  "images",
  "index.css",
  "altar.html",
  "arena.html",
  "boss.html",
  "ciudad.html",
  "combate.html",
  "estrategia.html",
  "formaciones.html",
  "heroes.html",
  "impel-down.html",
  "index.html",
  "instance.html",
  "leaderboard.html",
  "market.html",
  "materiales.html",
  "sistemas.html",
  "summon.html",
  "trial.html",
  "vegapunk.html",
  "video.html",
];

await rm(dist, { recursive: true, force: true });
await mkdir(dist, { recursive: true });

for (const entry of entries) {
  const source = path.join(root, entry);
  if (!existsSync(source)) continue;
  await cp(source, path.join(dist, entry), {
    recursive: true,
    force: true,
    filter: (sourcePath) => !sourcePath.toLowerCase().endsWith(".mp4"),
  });
}

await mkdir(path.join(dist, "server"), { recursive: true });
await writeFile(
  path.join(dist, "server", "index.js"),
  `import { readFile, stat } from "node:fs/promises";
import path from "node:path";

function getSiteRoot() {
  const cwd = process.cwd();
  if (path.basename(cwd) === "server") return path.resolve(cwd, "..");
  if (path.basename(cwd) === "dist") return cwd;
  return path.resolve(cwd, "dist");
}

const siteRoot = getSiteRoot();
const types = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".png": "image/png",
  ".webp": "image/webp",
  ".svg": "image/svg+xml",
  ".txt": "text/plain; charset=utf-8"
};

function cleanPath(url) {
  const parsed = new URL(url);
  const decoded = decodeURIComponent(parsed.pathname);
  const candidate = decoded === "/" ? "/index.html" : decoded;
  return candidate.replace(/^\\/+/g, "");
}

async function resolveFile(requestPath) {
  const direct = path.resolve(siteRoot, requestPath);
  if (!direct.startsWith(siteRoot)) return null;
  try {
    const info = await stat(direct);
    if (info.isFile()) return direct;
  } catch {}
  if (!path.extname(direct)) {
    const html = path.resolve(siteRoot, requestPath + ".html");
    if (!html.startsWith(siteRoot)) return null;
    try {
      const info = await stat(html);
      if (info.isFile()) return html;
    } catch {}
  }
  return null;
}

export async function fetch(request) {
  const requestPath = cleanPath(request.url);
  const file = await resolveFile(requestPath);
  if (!file) {
    return new Response("No encontrado", { status: 404 });
  }
  const body = await readFile(file);
  const ext = path.extname(file).toLowerCase();
  return new Response(body, {
    headers: {
      "content-type": types[ext] || "application/octet-stream",
      "cache-control": ext === ".html" ? "no-cache" : "public, max-age=31536000, immutable"
    }
  });
}

export default { fetch };
`,
  "utf-8",
);

console.log("Static wiki build ready in dist/");
