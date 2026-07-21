# USYD Bible · 悉尼大学新生终极手册

面向悉尼大学语言班（CET/DEC）及正式学位国际新生的中文非官方操作知识库。

## 在线网站

https://dreaminmaster.github.io/-usyd-guide-deploy/

## Official-first 版本

本版按照“先找第一手资料，再组织中文操作说明”的原则重构：

- 悉尼大学事务优先引用 USYD 与 CET 官方页面；
- 租房、交通、税务、工作权利和签证事项优先引用 NSW 或澳大利亚政府页面；
- 学生福利直接引用 USU 官方页面；
- 每篇重点指南展示官方路径、前置条件、分步操作、等待时间、风险提示、故障排查和原始链接；
- 个人 Offer、CoE、签证文件、学校邮件和登录后的系统信息始终高于本网站。

## 内容规模

- 423 个可搜索主题
- 280 篇操作指南
- 51 个常见问题
- 92 项可保存入学清单
- 50 个第一方或主管机构来源

## 重点内容

- CET/DEC 语言班与正式学位衔接
- Offer、CoE、签证条件、enrolment 与选课
- UniKey、Okta、Sydney Student、MyUni、Canvas、课表和 Wi-Fi
- 数字学生证、Transact eAccounts、Apple Wallet 与实体卡领取
- 学习方法、考试、特殊考虑、学术诚信与生成式 AI
- 图书馆、校园设施、医疗、心理支持与紧急求助
- 租房、交通、银行、电话卡、生活成本与学生福利
- 合法工作、TFN、求职、职业服务与工程专业规划

## 设计与交互

页面改为简洁的学校网站式信息架构，支持：

- 首页自然语言即时搜索与结果建议；
- `Ctrl/Command + K` 快速聚焦搜索；
- 热门问题快捷入口；
- 全站搜索与分类浏览；
- 文章内官方路径、步骤、警告、排查和来源；
- 收藏、文章深链接、深浅色模式和打印清单；
- `localStorage` 保存个人进度；
- 手机与桌面响应式布局。

## 构建与完整性

完整静态页面以经过哈希校验的 Base64/Gzip 分片保存在 `payload-v2/`。GitHub Actions 会：

1. 校验每个分片的 SHA-256；
2. 合并、解码和解压页面；
3. 核对最终 HTML 字节数与 SHA-256；
4. 检查关键内容标记；
5. 仅在全部验证通过后发布到 GitHub Pages。

最终内容 SHA-256：

`870213a38ef91c0c882e37d76ec78fc5d0d5669de35c836e5591fd5b684ecdbf`

元数据见 [`content-manifest.json`](./content-manifest.json)，验证脚本见 [`scripts/verify_payload.py`](./scripts/verify_payload.py)，线上发布结果见 [`DEPLOYMENT_STATUS.md`](./DEPLOYMENT_STATUS.md)，线上响应校验见 [`ONLINE_QA.md`](./ONLINE_QA.md)。

## 部署

Pages 发布源使用 **GitHub Actions**。推送到 `main` 后自动验证并重新部署；构建失败会记录到 `BUILD_STATUS.md`，不会覆盖当前线上版本。
