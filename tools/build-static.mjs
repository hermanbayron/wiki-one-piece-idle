import { cp, mkdir, rm } from "node:fs/promises";
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

console.log("Static wiki build ready in dist/");
