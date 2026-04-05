#!/usr/bin/env node
/**
 * Export "India Breathes" animation as a sequence of PNG frames.
 * Then stitch into GIF using Pillow (Python).
 *
 * Usage:
 *   node scripts/export_gif.js [--frames 365] [--width 1200] [--fps 15]
 *
 * Requires:
 *   - puppeteer (npm install puppeteer)
 *   - A local HTTP server serving web/ on port 8080
 *   - Python with Pillow for GIF stitching (run the printed command after)
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const args = process.argv.slice(2);
function getArg(name, def) {
  const i = args.indexOf(name);
  return i !== -1 && args[i + 1] ? args[i + 1] : def;
}

const TOTAL_FRAMES = parseInt(getArg('--frames', '365'));
const WIDTH = parseInt(getArg('--width', '1200'));
const FPS = parseInt(getArg('--fps', '15'));
const STEP = Math.max(1, Math.floor(365 / TOTAL_FRAMES));
const URL = getArg('--url', 'http://localhost:8080/breathes.html');

const OUT_DIR = path.join(__dirname, '..', 'art', 'output', 'gif_frames');
const OUT_GIF = path.join(__dirname, '..', 'art', 'output', 'india_breathes_2025.gif');

async function main() {
  // Create output directory
  if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });

  console.log(`Launching browser (${WIDTH}px wide)...`);
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', `--window-size=${WIDTH},900`],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: WIDTH, height: 900, deviceScaleFactor: 1 });

  console.log(`Loading ${URL}...`);
  await page.goto(URL, { waitUntil: 'networkidle0', timeout: 30000 });
  // Wait for D3 to finish rendering
  await page.waitForSelector('.region-path', { timeout: 10000 });
  await new Promise(r => setTimeout(r, 1000));

  // Hide the particle canvas (doesn't render well in screenshots)
  await page.evaluate(() => {
    const c = document.getElementById('seasonCanvas');
    if (c) c.style.display = 'none';
  });

  const totalSteps = Math.ceil(365 / STEP);
  console.log(`Capturing ${totalSteps} frames (every ${STEP} day(s))...`);

  for (let frame = 0; frame < totalSteps; frame++) {
    const day = Math.min(frame * STEP, 364);

    // Set the day via the page's updateAll function
    await page.evaluate((d) => { updateAll(d); }, day);
    // Small delay for transitions to settle
    await new Promise(r => setTimeout(r, 50));

    const framePath = path.join(OUT_DIR, `frame_${String(frame).padStart(4, '0')}.png`);
    await page.screenshot({ path: framePath, fullPage: true });

    if (frame % 50 === 0 || frame === totalSteps - 1) {
      console.log(`  Frame ${frame + 1}/${totalSteps} (day ${day})`);
    }
  }

  await browser.close();
  console.log(`\nFrames saved to: ${OUT_DIR}`);
  console.log(`\nTo create GIF, run:`);
  console.log(`  python3 scripts/stitch_gif.py --fps ${FPS}`);
}

main().catch(err => { console.error(err); process.exit(1); });
