# Word 与合作图渲染脚本

依赖：Python 3、python-docx、matplotlib、networkx。中文显示需要环境安装中文字体（如 Noto Sans CJK SC、Microsoft YaHei 或 SimHei）。脚本不下载字体、不安装依赖、不联网。

先复制 templates/evidence_template.json 并填入核验后的数据，删除空白占位项。所有 sources 引用必须指向台账中 verified=true 且 URL 有效的来源；未核实的内容写入 limitations，不作为已核实事实。

运行：python scripts/build_report.py evidence.json --out output_directory

输出：physician_brief_<姓名>_<日期>_<版本>.docx，以及临时子目录中的 network.png。只向最终用户返回 Word；图嵌入 Word。空模板可用于检查脚本是否运行，但不是医生研究结果。网络图是证据数据图，不是 AI 生成的装饰图。四卡用 Word 原生表格呈现，无人格评分。

必须检查最终文档；有文档渲染工具时转为页图并逐页查看，修复乱码、分页和表格溢出。脚本本身不完成视觉 QA，不自动检索、不自动核验来源真实性、不声称覆盖全网。
