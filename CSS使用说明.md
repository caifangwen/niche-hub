# NicheHub CSS 使用说明

本文档说明 NicheHub 项目五个核心 CSS 文件的结构、用途与使用规范。所有样式采用 **CSS 变量（Custom Properties）** 驱动，便于统一维护与主题切换。

---

## 文件概览

| 文件 | 体积 | 作用范围 | 说明 |
|------|------|----------|------|
| `nichehub-core.css` | ~20 KB | 全站 | 设计令牌、CSS 重置、基础排版、布局网格、工具类 |
| `nichehub-ui.css` | ~73 KB | 全站 | UI 组件：按钮、标签、卡片、表格、对比、TOC 等 |
| `nichehub-content.css` | ~15 KB | 全站 | 内容区块：Hero、FAQ、CTA、钢材卡片、OEM 注释 |
| `nichehub-dataviz.css` | ~14 KB | 数据页 | 数据可视化：进度条、热图、矩阵、评分、统计 |
| `nichehub-responsive.css` | ~4 KB | 全站 | 响应式断点覆盖与打印样式 |

**加载顺序建议：**

```html
<link rel="stylesheet" href="nichehub-core.css">
<link rel="stylesheet" href="nichehub-ui.css">
<link rel="stylesheet" href="nichehub-content.css">
<link rel="stylesheet" href="nichehub-dataviz.css">
<link rel="stylesheet" href="nichehub-responsive.css">
```

---

## 1. nichehub-core.css — 设计系统核心

### 1.1 设计令牌（Design Tokens）

所有视觉常量集中在 `:root` 中，分为以下几组：

#### 品牌色
```css
--primary: #1a1a1a;          /* 主色调（标题、深色背景） */
--secondary: #E53E3E;        /* 强调色（按钮、链接、边框） */
--secondary-hover: #C53030;  /* 强调色悬停态 */
```

#### 灰阶与文字色
```css
--text: #333333;             /* 正文色 */
--muted-900 ~ --muted-50    /* 9 级灰阶，数字越大越浅 */
--ink: #1a1a1a;              /* 最深文字色 */
```

#### 表面色（Surface）
```css
--surface: #fff;             /* 纯白背景 */
--surface-faq: #f5f5f5;      /* FAQ 区块背景 */
--surface-chip: #f0f0f0;     /* 标签/芯片背景 */
--surface-placeholder: #eee; /* 图片占位背景 */
```

#### 间距系统
```css
--gap-xs: 6px;
--gap-sm: 8px;
--gap-md: 10px;
--gap-lg: 14px;
--gap-xl: 16px;
--gap-2xl: 18px;
--gap-3xl: 20px;
--gap-4xl: 24px;
```

#### 圆角与阴影
```css
--r-8: 4px;   --r-10: 4px;   --r-12: 6px;
--shadow-1: 0 2px 8px rgba(0,0,0,0.04);
--shadow-5: 0 8px 24px rgba(0,0,0,0.07);
```

### 1.2 布局工具类

| 类名 | 用途 |
|------|------|
| `.container` | 居中容器，最大宽度 1200px |
| `.two-col` | 双列网格（移动端自动堆叠） |
| `.content-max` | 最大宽度 900px，用于正文区域 |
| `.text-center` / `.text-left` | 文字对齐 |
| `.mt-xs` ~ `.mt-4xl` | 上边距工具类（对应 --gap-*） |
| `.mb-md` ~ `.mb-2xl` | 下边距工具类 |
| `.text-secondary` | 强调色文字 |

### 1.3 Niche 文章系统（.nc-post）

`.nc-post` 是长文内容的命名空间，内部使用 `--nc-*` 变量隔离，避免与主样式冲突：

```html
<article class="nc-post">
  <h1>文章标题</h1>
  <p>正文段落...</p>
  <blockquote>引用内容</blockquote>
</article>
```

内置样式覆盖：h1~h6、段落、列表、代码块、表格、引用块。

---

## 2. nichehub-ui.css — UI 组件库

### 2.1 按钮与标签

```html
<!-- 实心按钮 -->
<a href="#" class="btn">了解更多</a>

<!-- 文字按钮 -->
<a href="#" class="btn-text">查看详情</a>

<!-- 价格标签 -->
<span class="tag budget">入门款</span>
<span class="tag mid">中端</span>
<span class="tag high">高端</span>
```

### 2.2 卡片体系

UI 文件包含大量卡片组件，命名规律如下：

| 前缀 | 用途 |
|------|------|
| `.product-*` | 产品展示卡片 |
| `.region-*` | 地区/产区卡片 |
| `.profile-*` | 钢材/品牌档案卡片 |
| `.vs-*` | 对比页面组件 |
| `.decision-*` | 决策流程组件 |
| `.care-*` | 保养指南组件 |
| `.timeline-*` | 时间线组件 |

**统一卡片结构示例：**

```html
<div class="profile-card">
  <div class="profile-card-header">
    <h4>钢材名称</h4>
    <span class="origin">产地</span>
  </div>
  <p class="profile-desc">描述文字...</p>
  <dl class="profile-specs">
    <dt>硬度</dt><dd>60 HRC</dd>
    <dt>耐腐蚀</dt><dd>中等</dd>
  </dl>
</div>
```

### 2.3 Niche 组件系统（.nc-*）

第二套组件命名空间，同样使用 `--nc-*` 变量，适合富媒体内容：

```html
<!-- 信息框 -->
<div class="nc-box">
  <span class="nc-box-title">核心要点</span>
  <ul>
    <li>要点一</li>
    <li>要点二</li>
  </ul>
</div>

<!-- 步骤流程 -->
<div class="nc-steps">
  <div class="nc-step">
    <div class="nc-step-n">01</div>
    <h4>步骤标题</h4>
    <p>步骤说明...</p>
  </div>
</div>
```

---

## 3. nichehub-content.css — 内容区块

### 3.1 Hero 与统计条

```html
<header>
  <div class="container">
    <div class="crumbs"><a href="#">首页</a> / <span>当前页</span></div>
    <div class="pillar-kicker">钢材百科</div>
    <h1>页面大标题</h1>
    <p class="hero-lead">导语文字...</p>
    <div class="stats-strip">
      <div class="stat-item">
        <span class="stat-val">52</span>
        <span class="stat-title">种钢材</span>
        <p class="stat-desc">涵盖碳钢、不锈钢、粉末钢...</p>
      </div>
    </div>
  </div>
</header>
```

### 3.2 钢材专属卡片（.steel-card）

```html
<div class="steel-card">
  <div class="steel-card-header">
    <span class="tag">高端</span>
    <h3>VG10</h3>
  </div>
  <p class="steel-card-lead">概述文字...</p>
  <div class="steel-card-main">
    <div class="steel-main-left">...</div>
    <div class="steel-main-right">...</div>
  </div>
  <div class="steel-card-footer">
    <div class="steel-links-row">
      <a href="#" class="btn-text">详细评测</a>
      <a href="#" class="btn-text">对比其他</a>
    </div>
  </div>
</div>
```

### 3.3 Steel Finder 交互组件

```html
<div class="finder-box">
  <h2>找到最适合你的钢材</h2>
  <div class="finder-grid">
    <select class="finder-select"><option>用途...</option></select>
    <select class="finder-select"><option>预算...</option></select>
  </div>
  <div class="finder-result">
    <div class="result-item">...</div>
  </div>
</div>
```

---

## 4. nichehub-dataviz.css — 数据可视化

### 4.1 比较条（Comparison Bars）

```html
<div class="d-row">
  <span class="d-name">硬度</span>
  <span class="d-score">9/10</span>
  <div class="d-bar"><div class="d-bar-fill" style="width:90%"></div></div>
</div>
```

### 4.2 Niche 数据图表

```html
<!-- 水平条形图 -->
<div class="nc-bars">
  <span class="nc-bars-title">性能对比</span>
  <div class="nc-bar-row">
    <span class="nc-bar-label">硬度</span>
    <div class="nc-bar-track"><div class="nc-bar-fill" style="width:85%"></div></div>
    <span class="nc-bar-val">85</span>
  </div>
</div>

<!-- 热图 -->
<div class="nc-heatmap">
  <div class="nc-heatmap-header">
    <div class="nc-heatmap-cell nc-heatmap-corner"></div>
    <div class="nc-heatmap-cell nc-heatmap-head">指标 A</div>
    <div class="nc-heatmap-cell nc-heatmap-head">指标 B</div>
  </div>
  <div class="nc-heatmap-row">
    <div class="nc-heatmap-cell nc-heatmap-label">钢材 X</div>
    <div class="nc-heatmap-cell nc-heatmap-high">高</div>
    <div class="nc-heatmap-cell nc-heatmap-mid">中</div>
  </div>
</div>
```

---

## 5. nichehub-responsive.css — 响应式规则

### 5.1 断点定义

| 断点 | 目标设备 |
|------|----------|
| `max-width: 820px` | 平板 / 小型桌面 |
| `max-width: 640px` | 大屏手机 |
| `max-width: 580px` | 中等手机 |
| `max-width: 560px` | 小屏手机 |
| `max-width: 540px` | 超小屏手机 |
| `max-width: 380px` | 迷你设备 |

### 5.2 常见覆盖模式

在断点内，绝大多数网格会从多列变为单列：

```css
@media (max-width: 820px) {
  .family-row { grid-template-columns: 1fr; }
  .two-col { grid-template-columns: 1fr; }
  .steel-card-main { grid-template-columns: 1fr; }
}
```

**开发提示：** 新增网格组件时，建议在此文件的 `820px` 断点内添加对应的 `1fr` 回退，保持移动端体验一致。

---

## 6. 命名规范

### 6.1 主命名空间（无前缀）
- 通用组件直接以功能命名：`.btn`、`.tag`、`.card`
- 模块级组件使用 BEM 风格：`.steel-card-header`、`.finder-result`

### 6.2 Niche 命名空间（.nc-）
- 用于富媒体文章、数据图表、复杂交互组件
- 变量隔离：`--nc-*` 与主变量 `--*` 互不干扰
- 适合需要独立排版体系的落地页内容

### 6.3 变量命名规律

| 前缀 | 含义 |
|------|------|
| `--primary` / `--secondary` | 品牌主色与强调色 |
| `--surface-*` | 背景/表面色 |
| `--muted-*` | 灰阶文字色（900 最深，50 最浅） |
| `--gap-*` | 间距尺度 |
| `--r-*` | 圆角半径 |
| `--shadow-*` | 阴影层级（1 最浅，6 最深） |
| `--nc-*` | Niche 命名空间变量 |

---

## 7. 添加新组件的最佳实践

1. **优先使用变量**：不要写死颜色或间距，始终引用 `--primary`、`--gap-lg` 等令牌。
2. **选择正确的文件**：
   - 基础工具类 / 排版 → `core`
   - 通用 UI 卡片 / 按钮 → `ui`
   - 页面专属内容块 → `content`
   - 图表 / 数据展示 → `dataviz`
   - 断点覆盖 → `responsive`
3. **移动端先行**：在写网格布局时，先在 `responsive.css` 的 `820px` 断点内写好单列回退。
4. **保持选择器扁平**：避免过度嵌套，尽量使用单一类名或浅层后代选择器。

---

## 8. 文件注释结构说明

每个 CSS 文件按功能区块组织，注释格式统一如下：

```css
/*
 * 区块名称
 * 简要描述该区块的作用。
 * ----------------------------------------------------------------------------- */
```

区块之间以空行分隔，便于快速定位与折叠编辑。
