from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
import textwrap

# 示例关联信息
SAMPLE_DOMAIN = "https://indexsite-leyu.com.cn"
KEYWORD = "乐鱼体育"
SEED = "c3bdb81f0c166e13"


@dataclass
class KeywordNote:
    """表示一条带有关键词和关联信息的笔记记录。"""
    title: str
    content: str
    keyword: str = KEYWORD
    source_url: Optional[str] = SAMPLE_DOMAIN
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    def formatted_summary(self, max_line_length: int = 60) -> str:
        """返回格式化的摘要信息，用于展示或日志输出。"""
        lines = []
        lines.append(f"标题: {self.title}")
        lines.append(f"关键词: {self.keyword}")
        lines.append(f"来源: {self.source_url or '无'}")
        lines.append(f"创建时间: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        if self.tags:
            lines.append(f"标签: {', '.join(self.tags)}")
        content_preview = (
            self.content[:50] + "..." if len(self.content) > 50 else self.content
        )
        wrapped = textwrap.fill(f"内容: {content_preview}", width=max_line_length)
        lines.append(wrapped)
        return "\n".join(lines)

    def to_dict(self) -> dict:
        """将笔记转换为字典，便于序列化或进一步处理。"""
        return {
            "title": self.title,
            "content": self.content,
            "keyword": self.keyword,
            "source_url": self.source_url,
            "tags": self.tags,
            "created_at": self.created_at.isoformat(),
        }


def generate_example_notes() -> List[KeywordNote]:
    """生成一组示例笔记，用于演示或测试。"""
    notes = [
        KeywordNote(
            title="行业动态",
            content="近期乐鱼体育平台在用户体验方面进行了多项优化，包括更流畅的直播观看体验和更丰富的体育赛事数据。",
            tags=["体育", "动态", "体验"],
        ),
        KeywordNote(
            title="技术更新",
            content="后端服务升级至最新架构，支持高并发访问和实时数据同步，确保用户获得稳定可靠的服务。",
            tags=["技术", "后端", "架构"],
            source_url=f"{SAMPLE_DOMAIN}/tech-update",
        ),
        KeywordNote(
            title="用户反馈",
            content="多数用户对平台界面简洁度和操作便捷性表示满意，部分用户建议增加更多体育项目分类。",
            tags=["用户", "反馈", "建议"],
        ),
    ]
    return notes


def output_notes(notes: List[KeywordNote]) -> None:
    """将笔记列表以格式化文本输出到标准输出。"""
    for i, note in enumerate(notes, 1):
        print(f"========== 笔记 {i} ==========")
        print(note.formatted_summary())
        print()


if __name__ == "__main__":
    print(f"关联域名: {SAMPLE_DOMAIN}")
    print(f"核心关键词: {KEYWORD}")
    print(f"种子标识: {SEED}")
    print()
    example_notes = generate_example_notes()
    output_notes(example_notes)