# USYD Bible · 悉尼大学新生终极手册

面向悉尼大学语言班（CET/DEC）及正式学位国际新生的中文非官方操作知识库。

## 在线网站

https://dreaminmaster.github.io/-usyd-guide-deploy/

## 内容留在本站，来源清楚标注

用户不需要跳转到学校官网才能读完一项操作。本站把完整中文说明、前置条件、步骤、等待时间、例外和故障排查保留在文章内；原始网页链接折叠在文末，仅供需要时核验。

正文使用四类可见标注：

- **官方事实**：直接来自 USYD、CET、澳大利亚政府或 NSW 政府公开页面，用于规则、资格、日期和明确步骤；
- **官方系统路径**：把官方页面中的菜单、按钮和先后顺序整理成中文操作路径，以登录后实际界面为准；
- **学生经验**：仅在存在具体、可识别来源时使用，用于补充实际体验，不能覆盖官方规则；
- **编辑整理**：根据官方资料形成的准备清单、排查顺序和风险提醒，不冒充学校规定。

个人 Offer、CoE、签证文件、学校邮件和登录后的 Sydney Student、Canvas 等系统记录，始终高于通用网站内容。

## 内容规模

- 423 个可搜索主题
- 280 篇操作指南
- 51 个常见问题
- 92 项可保存入学清单
- 50 个第一方或主管机构原始来源

## 重点内容

- CET/DEC 语言班与正式学位衔接
- Offer、CoE、签证条件、enrolment 与选课
- UniKey、Okta、Sydney Student、MyUni、Canvas、课表和 Wi-Fi
- 数字学生证、Transact eAccounts、Apple Wallet、丢失停用与恢复
- 学习方法、考试、特殊考虑、学术诚信与生成式 AI
- 图书馆、校园设施、医疗、心理支持与紧急求助
- 租房、交通、银行、电话卡、生活成本与学生福利
- 合法工作、TFN、求职、职业服务与工程专业规划

## 设计与交互

页面采用简洁的学校网站式信息架构，支持：

- 首页自然语言即时搜索与结果建议；
- `Ctrl/Command + K` 快速聚焦搜索；
- 全站搜索、热门问题入口与分类浏览；
- 文章内分段来源标签；
- 外部原始网页按需展开，而不是强制跳转；
- 收藏、文章深链接、深浅色模式和打印清单；
- `localStorage` 保存个人进度；
- 手机与桌面响应式布局。

## Apple Wallet 深度流程

数字学生证文章在本站内覆盖：

1. enrolment、UniKey、Okta 和照片审批准备；
2. 下载 Transact eAccounts 并选择 University of Sydney；
3. 添加到 iPhone Apple Wallet；
4. 添加到 Apple Watch；
5. 门禁、图书馆、打印和交通证明的同步等待时间；
6. 手机或手表丢失后的 Card Management / SydPay 停用；
7. 找回设备后的重新启用；
8. 考试必须携带实体学生证等例外。

## 构建与完整性

基础知识库仍以经过哈希校验的 Base64/Gzip 分片保存在 `payload-v2/`。来源标注系统使用可直接审阅的：

- [`assets/source-labels.css`](./assets/source-labels.css)
- [`assets/source-labels.js`](./assets/source-labels.js)

GitHub Actions 会：

1. 校验每个基础内容分片；
2. 解码、解压并核对基础 HTML；
3. 分别校验来源样式和来源逻辑资源；
4. 将两个资源引用注入发布页面；
5. 核对最终 HTML 字节数与 SHA-256；
6. 只有全部通过才发布到 GitHub Pages。

最终发布 HTML SHA-256：

`5cdacc4e0193b85ee7e8f809000bb3791b681e3dd5dfcbff8886fbabbe140b31`

元数据见 [`content-manifest.json`](./content-manifest.json)，验证脚本见 [`scripts/verify_payload.py`](./scripts/verify_payload.py)，部署结果见 [`DEPLOYMENT_STATUS.md`](./DEPLOYMENT_STATUS.md)，线上响应校验见 [`ONLINE_QA.md`](./ONLINE_QA.md)。

## 部署

Pages 发布源使用 **GitHub Actions**。推送到 `main` 后自动验证并重新部署；构建失败会记录到 `BUILD_STATUS.md`，不会覆盖当前线上版本。
