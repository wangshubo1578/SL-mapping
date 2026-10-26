# SL-mapping

**面向医学事务部门的医生公开学术信息研究 Skill。**  
**A physician public academic information research skill for Medical Affairs teams.**

SL-mapping 专为医学事务部门的学术交流准备与公开证据整理场景设计，不是通用个人背景调查、销售画像或性格分析工具。
SL-mapping is designed specifically for Medical Affairs workflows, including scientific engagement preparation and public evidence organization. It is not a general-purpose background investigation, sales profiling, or personality analysis tool.

## 适用对象与用途 | Intended Users & Use Cases

- **适用对象：**医学事务部门的医学科学联络官（MSL）、医学顾问及相关医学事务人员。  
  **Intended users:** Medical Science Liaisons (MSLs), Medical Advisors, and other Medical Affairs professionals.
- **主要用途：**整理医生公开职业背景、研究成果与学术合作证据，为科学交流准备材料。  
  **Primary purpose:** Organize physicians’ public professional backgrounds, research outputs, and documented academic collaborations to prepare for scientific discussions.
- **使用边界：**不用于临床诊疗决策、个人绩效评价、私人关系调查或基于人格推断的沟通操控。  
  **Boundaries:** Not intended for clinical decision-making, individual performance evaluation, private relationship investigation, or communication manipulation based on inferred personality.

## 核心功能 | Core Features

1. **输入与身份核验：**根据姓名、医院和科室核对医生身份，避免同名混淆。  
   **Input and identity verification:** Verify identity using name, hospital, and department to avoid mixing people with the same name.
2. **多渠道公开检索：**覆盖可访问的医院、学会、会议、期刊、试验登记和微信文章等公开来源。  
   **Multi-source public research:** Use accessible public sources such as hospitals, societies, conferences, journals, trial registries, and WeChat articles.
3. **职业与学术信息整理：**汇总基本信息、协会任职、职业生平及近五年最多五篇代表论文。  
   **Professional and academic summaries:** Summarize basic information, society appointments, career milestones, and up to five representative publications from the past five years.
4. **公开学术合作网络：**目标为中国机构与中国之外机构各最多十名有直接合作证据的医生，并绘制网络图。  
   **Public academic collaboration network:** Map up to ten collaborators at institutions in China and ten at institutions outside China, supported by direct collaboration evidence.
5. **学术沟通准备：**整理研究主题、证据问题、交流材料与待确认事项，不推断四色性格。  
   **Scientific engagement preparation:** Organize research themes, evidence questions, discussion materials, and items to confirm, without inferring four-color personality types.
6. **Word 输出与迭代：**生成带来源的报告，根据反馈另存新版并记录修改。  
   **Word output and iteration:** Produce source-linked reports and save revised versions with a change log following feedback.

## 证据与隐私原则 | Evidence & Privacy Principles

- 仅使用与专业用途相关的公开职业信息，不绕过登录、付费墙或访问限制。  
  Use only public professional information relevant to the task; do not bypass logins, paywalls, or access restrictions.
- 区分事实、推断和建议；保留来源、日期、冲突与缺失信息。  
  Distinguish facts, inferences, and recommendations; preserve sources, dates, conflicts, and gaps.
- 公开合作不等于私人关系亲密度，不排名个人能力或绩效。  
  Public collaboration does not establish personal closeness; do not rank individual ability or performance.
- 不从照片或间接信号推断性别、年龄、人格、情绪或私人兴趣。  
  Do not infer gender, age, personality, emotions, or private interests from photos or indirect signals.
- 不保证穷尽全网；微信等来源可能无法检索或访问。  
  Exhaustive web coverage is not guaranteed; sources such as WeChat may be inaccessible or undiscoverable.

## 使用方式 | Usage

将 SKILL.md 及相关资源加载到支持自定义 Skill 的宿主。实际导入方式、联网权限、脚本执行和文件生成能力取决于平台及组织配置；本项目未在特定 Copilot Cowork 租户中验证兼容性。
Load SKILL.md and its resources into a host that supports custom skills. Import methods, network permissions, script execution, and file generation depend on the platform and organizational configuration. Compatibility with a specific Copilot Cowork tenant has not been verified.

**中文任务示例：**
> 请使用 SL-mapping。医生：<姓名>；医院：<医院>；科室：<科室>；截止日期：<日期>。仅使用公开职业信息，生成含来源、公开学术合作网络图和学术沟通准备的 Word 报告。缺失信息如实标明。

**English task example:**
> Use SL-mapping for physician <name>, hospital <hospital>, department <department>, as of <date>. Use public professional information only. Generate a Word report with sources, a documented academic collaboration network, and scientific discussion preparation. Clearly identify missing information.

**修订：**提供上一版报告及修改意见；新事实需核验，保留旧版并记录修改。  
**Revisions:** Provide the previous report and requested changes. Verify new facts, retain earlier versions, and record changes.

## 文件结构 | Repository Contents

| 路径 / Path | 说明 / Description |
|---|---|
| SKILL.md | Skill 入口与流程 / Skill entrypoint and workflow |
| references/ | 检索、核验与合作网络规范 / Research, verification, and collaboration network protocols |
| templates/ | 报告大纲与证据模板 / Report outline and evidence template |
| scripts/build_report.py | 将已核验 JSON 渲染为 Word 和网络图，不执行检索 / Render verified JSON into Word and a network figure; no research execution |
| scripts/package_skill.py | 白名单打包 / Allowlisted Skill packaging |
| tests/ | 自动测试与验收清单 / Automated tests and acceptance checklist |
| docs/PUBLISHING.md | 发布说明 / Publishing guide |
| .github/ | 自动化与反馈模板 / Automation and feedback templates |

## 开发与验证 | Development & Validation

需要 Python 3.10 或以上版本；使用以下命令安装依赖、运行测试并打包。  
Requires Python 3.10 or later. Install dependencies, run tests, and package the Skill with:

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/package_skill.py --out dist/sl-mapping.zip
```

自动测试覆盖入口结构、空模板 Word 生成、引用校验与白名单打包，不验证真实医生身份、网页可访问性、网络图完整性或最终 Word 视觉效果。依赖采用版本范围，未提供锁定环境。
Automated tests cover entrypoint structure, empty-template Word generation, citation validation, and allowlisted packaging. They do not verify real physician identities, webpage accessibility, network completeness, or final Word visual layout. Dependency ranges are provided, not a locked environment.

GitHub Actions 的远程结果以实际运行日志为准；本地测试通过不代表远程 CI 已运行。
Remote GitHub Actions results must be checked in the actual run logs; passing local tests does not mean remote CI has run.

## 作者与联系 | Author & Contact

- **作者与版权署名 / Author and copyright holder:** wangshubo1578
- **联系邮箱 / Contact email:** o_kihiro@163.com

普通问题、建议与合作意向可提交 Issue 或通过邮箱联系；安全或隐私问题请私下邮件联系，不要公开敏感细节。
For general questions, suggestions, or collaboration, open an Issue or contact the author by email. Report security or privacy concerns privately by email without posting sensitive details publicly.

## 项目声明 | Project Statement

本项目为个人开源项目，面向医学事务部门的专业工作场景，不代表任何雇主、医院或机构的观点或背书。使用者应遵守所在组织的政策与适用要求。不要向公开仓库提交真实医生报告、患者资料、企业内部材料或凭据。
This is a personal open-source project intended for Medical Affairs workflows. It does not represent the views or endorsement of any employer, hospital, or institution. Users should follow their organizational policies and applicable requirements. Do not submit real physician reports, patient information, internal company materials, or credentials to the public repository.

## 许可证与贡献 | License & Contributions

本项目使用 [MIT License](LICENSE)。该许可证适用于本项目文件，不授予第三方论文、网页或个人数据的使用权。发布前请确认该许可证符合你的意愿。
This project uses the [MIT License](LICENSE). It covers project files and does not grant rights to third-party papers, webpages, or personal data. Confirm that this license matches your intentions before publishing.

参见 [贡献指南](CONTRIBUTING.md)、[安全说明](SECURITY.md)、[行为准则](CODE_OF_CONDUCT.md) 与 [更新记录](CHANGELOG.md)。
See the [contribution guide](CONTRIBUTING.md), [security policy](SECURITY.md), [code of conduct](CODE_OF_CONDUCT.md), and [changelog](CHANGELOG.md).

## 名称说明 | Naming

项目展示名称为 SL-mapping；机器标识为 sl-mapping。两者指同一个 Skill。
The display name is SL-mapping; the machine identifier is sl-mapping. Both refer to the same Skill.
