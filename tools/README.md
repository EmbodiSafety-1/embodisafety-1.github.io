# 视频编辑入口

这是静态网站，没有单独的管理后台。下面的文件控制视频和文案。

## Demo 展区

编辑 `assets/demos/manifest.json`。每个对象是一条视频，数组顺序就是展示顺序：

- `src`：MP4 文件路径。
- `poster`：播放前海报路径。
- `title`：卡片标题。
- `instruction`：标题下方的 caption。
- `environment`：环境筛选分类。

视频循环播放到文件结尾；修改实际 MP4 才能改变播放时长，添加或修改 JSON 的 duration 字段不会裁切视频。

改完执行 `python tools/build_page.py`，把配置重新写入 `index.html`，然后刷新浏览器。

## 首屏连续视频

编辑 `tools/prepare_hero.py` 开头的 `selected` 列表，设置三段视频的文件名、顺序及画面水平焦点百分比。视频位于 `assets/videos/`；对应海报位于 `assets/posters/`，文件名相同。

首屏源片要求 H.264、1280×720、24fps、无音轨。修改时长要先裁切源 MP4；本脚本根据帧数自动计算每段 start、duration、end。需要系统安装 FFmpeg（ffmpeg / ffprobe）。

依次执行：

```powershell
python tools/prepare_hero.py
python tools/build_page.py
```

前者重新生成 `assets/videos/hero-examples.mp4` 和 `assets/hero-chapters.json`；后者更新页面内嵌的章节数据。单独修改章节 JSON 不会重新剪辑视频。

首屏按要求仅显示编号，没有 caption。要新增首屏文字，请修改 `tools/build_page.py` 的 hero 模板；播放进度和章节切换逻辑在 `app.js`。

## 预览

在项目根目录执行 `python preview.py`，打开 http://127.0.0.1:8766/ 。不要重复启动已在运行的预览服务。
