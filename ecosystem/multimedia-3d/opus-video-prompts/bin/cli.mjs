#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');
const dataFile = path.join(rootDir, 'data', 'videos.json');

if (!fs.existsSync(dataFile)) {
  console.error(`[Error] Data file not found: ${dataFile}`);
  process.exit(1);
}

const videos = JSON.parse(fs.readFileSync(dataFile, 'utf8'));

const args = process.argv.slice(2);
const command = args[0] ? args[0].toLowerCase() : 'help';

function showHelp() {
  console.log(`
\x1b[36m=====================================================\x1b[0m
\x1b[1m\x1b[32m  Awesome Opus 5.5 AI Video Prompts CLI\x1b[0m
\x1b[36m=====================================================\x1b[0m
Total curated entries: \x1b[33m${videos.length}\x1b[0m

\x1b[1mCommands:\x1b[0m
  \x1b[32mopus-video stats\x1b[0m                Show summary statistics and categories
  \x1b[32mopus-video categories\x1b[0m           List all video categories with counts
  \x1b[32mopus-video search <keyword>\x1b[0m     Search video prompts by keyword
  \x1b[32mopus-video random [category]\x1b[0m    Get a random high-quality prompt (optionally filter by category)
  \x1b[32mopus-video get <slug>\x1b[0m           Print full prompt details for a specific slug
  \x1b[32mopus-video help\x1b[0m                 Show this help message

\x1b[1mExamples:\x1b[0m
  opus-video search motion
  opus-video search "3d typography"
  opus-video random UI/UX
  opus-video stats
`);
}

function showStats() {
  const catMap = {};
  for (const v of videos) {
    const c = v.category || 'Uncategorized';
    catMap[c] = (catMap[c] || 0) + 1;
  }
  console.log(`\n\x1b[1mTotal Videos:\x1b[0m ${videos.length}\n`);
  console.log(`\x1b[1mCategories Breakdown:\x1b[0m`);
  for (const [c, count] of Object.entries(catMap).sort((a,b) => b[1] - a[1])) {
    console.log(`  - \x1b[36m${c}\x1b[0m: ${count} videos`);
  }
  console.log();
}

function showCategories() {
  const catMap = {};
  for (const v of videos) {
    const c = v.category || 'Uncategorized';
    catMap[c] = (catMap[c] || 0) + 1;
  }
  console.log(`\n\x1b[1mAvailable Categories:\x1b[0m`);
  for (const [c, count] of Object.entries(catMap).sort((a,b) => b[1] - a[1])) {
    console.log(`  * \x1b[33m${c}\x1b[0m (${count})`);
  }
  console.log();
}

function searchVideos(query) {
  if (!query) {
    console.log('\x1b[31mPlease provide a keyword to search.\x1b[0m Example: opus-video search motion');
    return;
  }
  const q = query.toLowerCase();
  const results = videos.filter(v => {
    return (v.slug && v.slug.toLowerCase().includes(q)) ||
           (v.category && v.category.toLowerCase().includes(q)) ||
           (v.prompt && v.prompt.toLowerCase().includes(q)) ||
           (Array.isArray(v.tech_tags) && v.tech_tags.some(t => t.toLowerCase().includes(q)));
  });

  console.log(`\nFound \x1b[32m${results.length}\x1b[0m result(s) for "\x1b[33m${query}\x1b[0m":\n`);
  const displayLimit = Math.min(results.length, 10);
  for (let i = 0; i < displayLimit; i++) {
    const v = results[i];
    console.log(`\x1b[1m[${i + 1}] ${v.slug}\x1b[0m (${v.category || 'General'})`);
    if (v.tech_tags && v.tech_tags.length) {
      console.log(`    Tags: \x1b[35m${v.tech_tags.join(', ')}\x1b[0m`);
    }
    const snippet = v.prompt ? v.prompt.slice(0, 140).replace(/\r?\n|\r/g, ' ') : '';
    console.log(`    Prompt: \x1b[90m${snippet}...\x1b[0m`);
    if (v.post_url) console.log(`    Link: ${v.post_url}`);
    console.log();
  }
  if (results.length > displayLimit) {
    console.log(`... and ${results.length - displayLimit} more. Refine your query or use 'opus-video get <slug>'.\n`);
  }
}

function getRandom(categoryFilter) {
  let pool = videos;
  if (categoryFilter) {
    const cf = categoryFilter.toLowerCase();
    pool = videos.filter(v => v.category && v.category.toLowerCase().includes(cf));
    if (pool.length === 0) {
      console.log(`\x1b[31mNo videos found in category: ${categoryFilter}\x1b[0m`);
      pool = videos;
    }
  }
  const item = pool[Math.floor(Math.random() * pool.length)];
  console.log(`\n\x1b[36m==================== SELECTED OPUS PROMPT ====================\x1b[0m`);
  console.log(`\x1b[1mSlug:\x1b[0m ${item.slug}`);
  console.log(`\x1b[1mCategory:\x1b[0m ${item.category || 'N/A'}`);
  console.log(`\x1b[1mAuthor:\x1b[0m ${item.author || 'Anonymous'} (${item.author_url || ''})`);
  if (item.tech_tags && item.tech_tags.length) {
    console.log(`\x1b[1mTags:\x1b[0m \x1b[35m${item.tech_tags.join(', ')}\x1b[0m`);
  }
  if (item.post_url) console.log(`\x1b[1mOriginal Post:\x1b[0m ${item.post_url}`);
  console.log(`\n\x1b[1mFull Prompt:\x1b[0m\n\x1b[32m${item.prompt || 'No prompt content'}\x1b[0m\n`);
  console.log(`\x1b[36m==============================================================\x1b[0m\n`);
}

function getBySlug(slug) {
  if (!slug) {
    console.log('\x1b[31mPlease provide a slug.\x1b[0m Example: opus-video get <slug>');
    return;
  }
  const item = videos.find(v => v.slug === slug || (v.slug && v.slug.toLowerCase() === slug.toLowerCase()));
  if (!item) {
    console.log(`\x1b[31mVideo not found with slug:\x1b[0m ${slug}`);
    return;
  }
  console.log(`\n\x1b[1mSlug:\x1b[0m ${item.slug}`);
  console.log(`\x1b[1mCategory:\x1b[0m ${item.category || 'N/A'}`);
  console.log(`\x1b[1mAuthor:\x1b[0m ${item.author || 'Anonymous'} (${item.author_url || ''})`);
  if (item.tech_tags && item.tech_tags.length) {
    console.log(`\x1b[1mTags:\x1b[0m \x1b[35m${item.tech_tags.join(', ')}\x1b[0m`);
  }
  if (item.post_url) console.log(`\x1b[1mLink:\x1b[0m ${item.post_url}`);
  console.log(`\n\x1b[1mFull Prompt:\x1b[0m\n\x1b[32m${item.prompt}\x1b[0m\n`);
}

switch (command) {
  case 'stats':
    showStats();
    break;
  case 'categories':
  case 'cats':
    showCategories();
    break;
  case 'search':
  case 'find':
    searchVideos(args.slice(1).join(' '));
    break;
  case 'random':
  case 'rand':
    getRandom(args.slice(1).join(' '));
    break;
  case 'get':
    getBySlug(args[1]);
    break;
  case 'help':
  default:
    showHelp();
    break;
}
