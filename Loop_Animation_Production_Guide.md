# Lo-fi Loop 動畫製作指南 (Pika & AE 整合)

## 🎨 核心概念
Lo-fi 動畫的靈魂在於「氛圍 (Vibe)」與「循環性 (Looping)」。一個成功的 Loop 應該讓人感受不到起點與終點。

## 🛠 製作工具流
### 1. Pika (AI 影片生成)
- **基礎提示詞結構**: `[Subject] sitting in [Environment], [Specific Action], lofi style, flat illustration, anime aesthetic, warm lighting, muted colors, grainy texture --motion 1`
- **循環技巧**: 
    - 使用 `--loop` 參數 (如果支援)。
    - 生成短片段後，在剪輯軟體中進行「首尾淡入淡出 (Cross-dissolve)」處理。

### 2. After Effects (後製與細節)
- **顆粒感 (Grain)**: 加入 `Noise` 效果 (3-5%) 營造復古膠卷感。
- **色彩空間 (LUTs)**: 使用溫暖或褪色的調色，降低飽和度。
- **微動效果**: 
    - 使用 `Wiggle` 運算式處理燈光閃爍或灰塵粒子。
    - 加入漂浮的蒸汽或雨滴特效。

## 📝 《Midnight Coffee》動畫規劃
- **場景**: 雨夜的咖啡廳窗邊，一杯冒煙的咖啡。
- **動態**:
    - 背景：窗外雨滴滑落。
    - 中景：咖啡杯散發出的熱氣。
    - 前景：偶爾閃爍的檯燈。
- **技術指標**: 1080p, 24fps, 10秒循環。

## 📅 執行步驟
1. 使用 Midjourney 生成關鍵幀背景。
2. 使用 Pika 生成動態元素。
3. 匯入 AE 進行色彩校正與循環處理。
4. 最終渲染為 H.264 MP4。
