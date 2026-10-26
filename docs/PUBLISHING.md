# 发布说明

## 仓库信息建议
- 名称：sl-mapping
- 简介：Evidence-grounded physician public academic briefs with source tracking, collaboration networks, and Word reports.
- Topics：agent-skill, medical-affairs, evidence-synthesis, physician-research, docx, public-information

## 首次发布
1. 解压仓库包，将其中所有文件放在仓库根目录，保留 .github、.gitignore 等隐藏文件。
2. 检查 LICENSE。本包预置 MIT；若不符合你的意愿，发布前替换。版权署名已配置为 wangshubo1578。
3. 作者署名已配置为 wangshubo1578，联系邮箱为 o_kihiro@163.com。仓库地址未预填，请创建仓库后按需补充。
4. 检查没有真实医生报告、企业内部资料、凭据、私人数据和版权全文。
5. 创建 GitHub 仓库后上传文件，或在本地按 GitHub 给出的仓库地址推送。无需预先替换任何代码中的仓库 URL。
6. 查看 Actions 中 Validate 的运行结果；本地通过不等于 GitHub CI 已通过。
7. 可手动运行 Package Skill 下载白名单打包产物；也可本地执行下方命令。
8. 按需创建 v1.0.0 Release 并附上 Skill ZIP。工作流不自动创建 Release，也不自动修改仓库权限。

## 本地命令
```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/package_skill.py --out dist/sl-mapping.zip
```

## 三类文件不要混淆
- GitHub 仓库包：包含开发文档、测试和 .github 配置。
- Skill ZIP：只含运行所需指令、参考文件、模板和辅助脚本。
- 医生 Word 报告：运行后生成的研究输出，默认不提交公开仓库。

## 未自动完成的事项
未创建 GitHub 仓库、未上传、未启用仓库设置、未运行远程 CI、未验证 Cowork 安装兼容性。是否允许发布及使用公司相关成果由你自行确认；本包不代表雇主或任何医院背书。
