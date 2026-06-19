from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

# 关键词笔记配置
SITE_URL = "https://init-nangong28.com"
KEYWORD = "南宫28"

@dataclass
class KeywordNote:
    title: str
    content: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def summary(self, max_length: int = 50) -> str:
        """生成简短摘要"""
        if len(self.content) <= max_length:
            return self.content
        return self.content[:max_length] + "..."

    def format_with_keyword(self, keyword: str = KEYWORD) -> str:
        """将关键词嵌入笔记摘要"""
        return f"[{keyword}] {self.title}: {self.summary()}"


def format_notes_as_report(notes: List[KeywordNote], url: str = SITE_URL) -> str:
    """将一组笔记格式化为可读报告"""
    lines = [f"关键词笔记报告 - 来源: {url}", "=" * 40]
    for i, note in enumerate(notes, 1):
        lines.append(f"\n{i}. {note.title}")
        lines.append(f"   内容: {note.content}")
        if note.tags:
            lines.append(f"   标签: {', '.join(note.tags)}")
        lines.append(f"   创建时间: {note.created_at}")
        lines.append(f"   关键词摘要: {note.format_with_keyword()}")
    lines.append("\n" + "=" * 40)
    lines.append(f"共 {len(notes)} 条笔记")
    return "\n".join(lines)


def demo_usage():
    """演示用法"""
    notes = [
        KeywordNote(
            title="南宫28 平台介绍",
            content="这是一个综合性在线娱乐平台，提供多种游戏和服务。",
            tags=["平台", "娱乐"],
            created_at="2025-01-15 10:30:00"
        ),
        KeywordNote(
            title="使用技巧",
            content="用户可以通过访问 https://init-nangong28.com 获取更多信息。",
            tags=["技巧", "指南"]
        ),
        KeywordNote(
            title="安全提示",
            content="请妥善保管个人账户信息，避免在公共设备上登录。",
            tags=["安全", "提醒"]
        )
    ]
    print(format_notes_as_report(notes))


if __name__ == "__main__":
    demo_usage()