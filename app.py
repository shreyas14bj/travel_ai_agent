from pathlib import Path
import sys
import streamlit as st

# ──────────────────────────────────────────────────────────────────────────────
# Project bootstrap
# ──────────────────────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.agents import ask_rag, get_rag_status, rebuild_vectorstore


st.set_page_config(
    page_title="Voyage AI • Tourism Intelligence",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────────────────────────────────────
# Design system
# ──────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --bg: #f6f8fb;
    --surface: #ffffff;
    --surface-2: #f0f4f8;
    --ink: #15202b;
    --muted: #64748b;
    --line: #e2e8f0;
    --brand: #0f766e;
    --brand-2: #115e59;
    --accent: #d97706;
    --success: #15803d;
    --danger: #b91c1c;
    --shadow: 0 10px 30px rgba(15, 23, 42, .06);
}

html, body, [class*="css"] {
    font-family: "DM Sans", sans-serif;
    color: var(--ink);
}

.stApp {
    background:
        radial-gradient(circle at 82% 0%, rgba(15,118,110,.07), transparent 28rem),
        linear-gradient(180deg, #fbfcfd 0%, var(--bg) 100%);
}

.block-container {
    max-width: 1440px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

section[data-testid="stSidebar"] {
    background: #102a2a;
    border-right: 0;
}

section[data-testid="stSidebar"] * {
    color: #e7f5f2 !important;
}

section[data-testid="stSidebar"] .stButton > button {
    background: rgba(255,255,255,.06);
    border: 1px solid rgba(255,255,255,.08);
    color: #e7f5f2 !important;
    text-align: left;
    border-radius: 12px;
    min-height: 42px;
    transition: .18s ease;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(255,255,255,.12);
    border-color: rgba(255,255,255,.18);
    transform: translateX(2px);
}

.hero {
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(15,118,110,.12);
    border-radius: 24px;
    padding: 2.2rem 2.4rem;
    margin-bottom: 1.2rem;
    background:
        radial-gradient(circle at 95% 10%, rgba(217,119,6,.13), transparent 18rem),
        radial-gradient(circle at 72% 90%, rgba(15,118,110,.10), transparent 20rem),
        #fff;
    box-shadow: var(--shadow);
}

.hero h1 {
    font-family: "Playfair Display", serif;
    font-size: clamp(2.2rem, 4vw, 4rem);
    line-height: 1.05;
    margin: 0 0 .75rem 0;
    letter-spacing: -.035em;
}

.hero p {
    color: var(--muted);
    max-width: 760px;
    font-size: 1.02rem;
    line-height: 1.7;
    margin: 0;
}

.badge {
    display: inline-flex;
    align-items: center;
    gap: .45rem;
    padding: .35rem .7rem;
    border-radius: 999px;
    background: #e7f5f2;
    color: var(--brand-2);
    font-size: .78rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.section-title {
    font-family: "Playfair Display", serif;
    font-size: 1.55rem;
    margin: .4rem 0 .15rem;
}

.section-subtitle {
    color: var(--muted);
    margin-bottom: 1rem;
}

.feature-card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 1.1rem;
    min-height: 112px;
    box-shadow: 0 6px 18px rgba(15,23,42,.035);
}

.feature-icon {
    font-size: 1.35rem;
    margin-bottom: .35rem;
}

.feature-title {
    font-weight: 700;
    margin-bottom: .2rem;
}

.feature-copy {
    color: var(--muted);
    font-size: .84rem;
    line-height: 1.45;
}

.answer-card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-left: 4px solid var(--brand);
    border-radius: 18px;
    padding: 1.35rem 1.5rem;
    box-shadow: var(--shadow);
}

.chat-label {
    font-size: .78rem;
    font-weight: 700;
    color: var(--brand-2);
    text-transform: uppercase;
    letter-spacing: .08em;
    margin-bottom: .25rem;
}

.source-card {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 15px;
    padding: .85rem 1rem;
    margin-bottom: .6rem;
}

.source-meta {
    color: var(--muted);
    font-size: .78rem;
}

.status-pill {
    display: inline-block;
    padding: .28rem .62rem;
    border-radius: 999px;
    background: #ecfdf3;
    color: var(--success);
    font-weight: 700;
    font-size: .75rem;
}

div[data-testid="stMetric"] {
    background: var(--surface);
    border: 1px solid var(--line);
    padding: .85rem 1rem;
    border-radius: 15px;
    box-shadow: 0 5px 16px rgba(15,23,42,.03);
}

.stTextArea textarea {
    border-radius: 16px !important;
    border: 1px solid #d7dee8 !important;
    background: #fff !important;
    font-size: 1rem !important;
    padding: 1rem !important;
}

.stTextArea textarea:focus {
    border-color: var(--brand) !important;
    box-shadow: 0 0 0 3px rgba(15,118,110,.10) !important;
}

.stButton > button {
    border-radius: 11px;
    min-height: 42px;
    font-weight: 600;
    transition: .18s ease;
}

.stButton > button:hover {
    transform: translateY(-1px);
}

div[data-testid="stTabs"] button {
    font-weight: 600;
}

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: .78rem;
    padding-top: 1.5rem;
}
</style>
""",
    unsafe_allow_html=True,
)


# ──────────────────────────────────────────────────────────────────────────────
# State
# ──────────────────────────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "question": "",
        "answer": None,
        "sources": [],
        "history": [],
        "error": None,
        "active_tab": "chat",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def run_question(question: str):
    question = question.strip()
    if not question:
        st.session_state.error = "Please enter a tourism question."
        return False

    st.session_state.error = None

    try:
        with st.spinner("Voyage AI is searching the tourism knowledge base…"):
            answer, sources = ask_rag(question)

        st.session_state.question = question
        st.session_state.answer = answer
        st.session_state.sources = sources or []
        st.session_state.history.append(
            {
                "question": question,
                "answer": answer,
                "sources": sources or [],
            }
        )
        return True

    except Exception as exc:
        st.session_state.error = (
            "The assistant could not process that request. "
            f"{type(exc).__name__}: {exc}"
        )
        st.session_state.answer = None
        st.session_state.sources = []
        return False


def clear_session():
    st.session_state.question = ""
    st.session_state.answer = None
    st.session_state.sources = []
    st.session_state.history = []
    st.session_state.error = None


init_state()


# ──────────────────────────────────────────────────────────────────────────────
# Sidebar
# ──────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
        <div style="padding:.6rem 0 1rem;">
            <div style="font-size:1.65rem;font-weight:800;">🌍 Voyage AI</div>
            <div style="font-size:.78rem;opacity:.72;margin-top:.2rem;">
                Tourism Intelligence Platform
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Explore")
    quick_questions = {
        "🏝️ Destinations": "What are the best tourism destinations?",
        "🏨 Hotels & policies": "What are the important hotel policies?",
        "✈️ Trip planning": "Help me plan a tourism trip.",
        "🎒 Activities": "What activities and attractions are available?",
        "💰 Budget travel": "How can I plan a budget-friendly trip?",
        "⚠️ Travel advisory": "What travel advisories should I know?",
    }

    for label, prompt in quick_questions.items():
        if st.button(label, use_container_width=True):
            run_question(prompt)
            st.rerun()

    st.markdown("---")
    st.markdown("### Session")
    st.metric("Questions asked", len(st.session_state.history))

    if st.button("🗑️ Clear conversation", use_container_width=True):
        clear_session()
        st.rerun()

    st.markdown("---")
    st.caption("Knowledge-grounded RAG assistant")
    st.caption("Designed for tourism discovery, planning and research.")


# ──────────────────────────────────────────────────────────────────────────────
# Main hero
# ──────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="hero">
        <div class="badge">● AI-POWERED TOURISM INTELLIGENCE</div>
        <h1>Travel smarter.<br>Explore deeper.</h1>
        <p>
            Ask questions about destinations, hotels, activities, travel planning,
            budgets and tourism policies. Voyage AI retrieves relevant knowledge
            from your tourism database before generating an answer.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Feature strip
f1, f2, f3, f4 = st.columns(4)
features = [
    ("🧭", "Discover", "Explore destinations and tourism information."),
    ("🏨", "Stay", "Understand hotels, accommodation and policies."),
    ("🗺️", "Plan", "Build travel ideas around your knowledge base."),
    ("📚", "Grounded", "See the retrieved knowledge behind answers."),
]
for col, (icon, title, copy) in zip((f1, f2, f3, f4), features):
    with col:
        st.markdown(
            f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <div class="feature-title">{title}</div>
                <div class="feature-copy">{copy}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")

tab_chat, tab_sources, tab_history, tab_system = st.tabs(
    ["💬 AI Assistant", "📚 Knowledge Sources", "🕘 History", "⚙️ System"]
)

# ──────────────────────────────────────────────────────────────────────────────
# Assistant
# ──────────────────────────────────────────────────────────────────────────────
with tab_chat:
    st.markdown('<div class="section-title">What would you like to explore?</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Ask a natural-language question. The assistant will retrieve relevant tourism knowledge and formulate a response.</div>',
        unsafe_allow_html=True,
    )

    with st.form("tourism_question_form", clear_on_submit=False):
        question = st.text_area(
            "Tourism question",
            value=st.session_state.question,
            height=125,
            label_visibility="collapsed",
            placeholder=(
                "Ask anything about tourism…\n\n"
                "For example: Which destinations, activities and hotel options "
                "are available for a family trip?"
            ),
        )
        c1, c2, c3 = st.columns([1.7, 1, 5])
        with c1:
            ask_clicked = st.form_submit_button(
                "✨ Ask Voyage AI",
                type="primary",
                use_container_width=True,
            )
        with c2:
            clear_clicked = st.form_submit_button(
                "Clear",
                use_container_width=True,
            )

    if ask_clicked:
        run_question(question)
        st.rerun()

    if clear_clicked:
        clear_session()
        st.rerun()

    if st.session_state.error:
        st.error(st.session_state.error)

    if st.session_state.answer:
        st.write("")
        st.markdown(
            '<div class="chat-label">Voyage AI response</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="answer-card">',
            unsafe_allow_html=True,
        )
        st.markdown(st.session_state.answer)
        st.markdown("</div>", unsafe_allow_html=True)

        source_count = len(st.session_state.sources)
        st.caption(
            f"Grounded with {source_count} retrieved knowledge "
            f"{'chunk' if source_count == 1 else 'chunks'}."
        )
    else:
        st.info(
            "Start with a question above, or choose a popular topic from the sidebar."
        )


# ──────────────────────────────────────────────────────────────────────────────
# Sources
# ──────────────────────────────────────────────────────────────────────────────
with tab_sources:
    st.markdown('<div class="section-title">Retrieved knowledge</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">These are the source chunks returned by the tourism RAG pipeline for the current answer.</div>',
        unsafe_allow_html=True,
    )

    sources = st.session_state.sources

    if not sources:
        st.info("No retrieved knowledge is available yet. Ask the assistant a question first.")
    else:
        seen = set()
        count = 0

        for doc in sources:
            md = doc.metadata or {}
            source = md.get("source", "Unknown source")
            chunk_id = md.get("chunk_id", "")
            key = (source, chunk_id)

            if key in seen:
                continue

            seen.add(key)
            count += 1

            with st.expander(f"📄 {count}. {source}", expanded=(count == 1)):
                x1, x2, x3 = st.columns(3)
                with x1:
                    st.caption("DOMAIN")
                    st.write(md.get("domain", "General Tourism"))
                with x2:
                    st.caption("DESTINATION / ENTITY")
                    st.write(md.get("entity", "General"))
                with x3:
                    st.caption("RETRIEVAL SCORE")
                    st.write(md.get("retrieval_score", "N/A"))

                st.divider()
                st.markdown(doc.page_content)


# ──────────────────────────────────────────────────────────────────────────────
# History
# ──────────────────────────────────────────────────────────────────────────────
with tab_history:
    st.markdown('<div class="section-title">Conversation history</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Review questions and answers from this browser session.</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.history:
        st.info("Your questions will appear here after your first interaction.")
    else:
        for index, item in enumerate(reversed(st.session_state.history), start=1):
            with st.expander(f"💬 {item['question']}"):
                st.markdown("**Question**")
                st.write(item["question"])
                st.markdown("**Answer**")
                st.markdown(item["answer"])

                if item.get("sources"):
                    st.caption(
                        f"{len(item['sources'])} retrieved knowledge "
                        f"{'chunk' if len(item['sources']) == 1 else 'chunks'}"
                    )


# ──────────────────────────────────────────────────────────────────────────────
# System / admin
# ──────────────────────────────────────────────────────────────────────────────
with tab_system:
    st.markdown('<div class="section-title">RAG system</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Operational information for the tourism knowledge pipeline.</div>',
        unsafe_allow_html=True,
    )

    try:
        status = get_rag_status()

        if isinstance(status, dict):
            status_cols = st.columns(min(4, max(1, len(status))))
            for col, (key, value) in zip(status_cols, status.items()):
                with col:
                    st.metric(str(key).replace("_", " ").title(), str(value))
        else:
            st.json(status)

    except Exception as exc:
        st.error(
            f"Unable to initialize RAG status: {type(exc).__name__}: {exc}"
        )

    st.divider()
    st.markdown("### Knowledge base maintenance")
    st.caption(
        "Rebuild the vector database when the underlying tourism source data changes."
    )

    if st.button("🔄 Rebuild vector database", type="primary"):
        try:
            with st.spinner("Rebuilding tourism vectors…"):
                result = rebuild_vectorstore()

            st.success("Vector database rebuild completed.")

            if isinstance(result, dict):
                a, b, c, d = st.columns(4)
                a.metric("Source chunks", result.get("current_source_chunks", "—"))
                b.metric("New vectors", result.get("new_vectors_added", "—"))
                c.metric("Removed", result.get("stale_vectors_removed", "—"))
                d.metric("DB count", result.get("vector_db_count", "—"))

        except Exception as exc:
            st.error(
                f"Rebuild failed: {type(exc).__name__}: {exc}"
            )


st.markdown(
    """
    <div class="footer">
        🌍 Voyage AI · Tourism Intelligence Platform · Retrieval-Augmented Generation
    </div>
    """,
    unsafe_allow_html=True,
)
