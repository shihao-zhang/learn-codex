## Context

SVG 教学辅助图既要表达事实边界，也要帮助非工程读者快速建立第一眼理解。第一批 rollout 暴露了两个不同层级的问题：

- s01 是信息架构问题：所有节点大小、颜色饱和度和路径密度接近，导致主路径不够突出。
- s02 是布局完整性问题：模块实际重叠，已经超过“审美偏好”，属于可读性缺陷。

因此规范需要从“源码可 review”补充到“渲染后可读”。

## Visual QA Principles

本次沉淀四条长期规则：

1. 提交前必须渲染预览关键 SVG，不能只看 XML。
2. 主机制路径优先：FACT 主路径应占据最稳定的阅读轴，教学 failure path 放在下方或侧边。
3. 防遮挡：模块、文字、chip、箭头、图例之间必须留出可见空隙，连线不得穿过文字。
4. 降密度：当一个图同时包含主路径、失败路径、恢复路径、trace chip 和图例时，应把它拆成上中下或左中右三个层级。

## Scope

- 修 s01 `turn-loop.svg` 的主次层级。
- 修 s02 `event-interface.svg` 的模块重叠。
- 更新 s01/s02 companion Markdown 的 Manual QA。
- 更新 `docs/diagram-style-guide.md`。

## Validation

- 使用本地渲染方式生成 PNG 并目视核实 s01/s02。
- 运行 XML 解析检查。
- 运行 OpenSpec 和仓库检查。
