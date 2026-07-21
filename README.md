# USYD Bible · 悉尼大学新生终极手册

面向悉尼大学语言班（CET/DEC）及正式学位国际新生的中文非官方操作知识库。

## 在线网站

https://dreaminmaster.github.io/-usyd-guide-deploy/

## 最终版规模

- 417 个可搜索主题
- 274 篇操作指南
- 51 个常见问题
- 92 项可保存入学清单
- 45 个悉尼大学及澳大利亚官方来源

## 内容范围

- CET/DEC 语言班与正式学位衔接
- Offer、CoE、签证条件、enrolment 与选课
- UniKey、Okta、Sydney Student、MyUni、Canvas、课表和 Wi‑Fi
- 数字学生证、Transact eAccounts 与 Apple Wallet
- 学习方法、考试、特殊考虑、学术诚信与生成式 AI
- 图书馆、校园设施、医疗、心理支持与紧急求助
- 租房、交通、银行、电话卡、生活成本与学生福利
- 合法工作、TFN、求职、职业服务与工程专业规划

网站支持全站搜索、分类浏览、收藏、深浅色主题、文章深链接、可打印清单以及基于 `localStorage` 的个人进度保存，优先适配手机端。

> 所有个人 Offer、学校邮件、CoE、签证文件和悉尼大学官方系统中的信息，优先级均高于本网站。时间敏感或个人化事项应通过官方渠道确认。

## 构建与完整性

完整静态页面以经过哈希校验的 Base64/Gzip 分片保存在 `payload/`。GitHub Actions 会：

1. 校验每个分片的 SHA-256；
2. 合并、解码和解压页面；
3. 核对最终 HTML 字节数与 SHA-256；
4. 仅在全部验证通过后发布到 GitHub Pages。

最终内容 SHA-256：

`49780e25289d6729302b50e73e34216ebbcdec4483376557df4877106ba62fbb`

元数据见 [`content-manifest.json`](./content-manifest.json)，验证脚本见 [`scripts/verify_payload.py`](./scripts/verify_payload.py)，线上发布结果见 [`DEPLOYMENT_STATUS.md`](./DEPLOYMENT_STATUS.md)。

## 部署

Pages 发布源使用 **GitHub Actions**。推送到 `main` 后自动验证并重新部署；构建失败会记录到 `BUILD_STATUS.md`，不会覆盖当前线上版本。
