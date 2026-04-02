import wikipediaapi
import streamlit as st

class AlgorithmChatbot:
    def __init__(self):
        # Wikipedia requires a user-agent string (Name + Contact)
        self.wiki = wikipediaapi.Wikipedia(
            user_agent="AlgoBot/1.0 (contact@example.com)",
            language='en'
        )

        # Map of common aliases to their official Wikipedia page titles
        self.algo_map = {
            "bfs": "Breadth-first search",
            "dfs": "Depth-first search",
            "a*": "A* search algorithm",
            "ao*": "And–or graph",
            "hill climb": "Hill climbing",
            "best first search": "Best-first search"
        }

    def get_wiki_summary(self, topic):
        page = self.wiki.page(topic)
        if page.exists():
            return "\n".join(page.summary.split('\n')[:2])
        return "I found the topic, but I couldn't retrieve the details."

    def handle_query(self, user_input):
        user_input = user_input.lower()
        for key, wiki_title in self.algo_map.items():
            if key in user_input:
                return self.get_wiki_summary(wiki_title)

        return (
            "I'm specialized in BFS, DFS, A*, AO*, Hill Climbing, and Best First Search. "
            "Ask me about those!"
        )

def main():
    st.set_page_config(
        page_title="AlgoWiki AI",
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    # Main Header
    st.markdown(
        "<div style='background:#1f3c88;padding:24px;border-radius:16px;color:white;'>"
        "<h1 style='margin:0;'>AlgoWiki AI</h1>"
        "<p style='margin:8px 0 0;'>Ask about search algorithms and get concise Wikipedia summaries with a website-style chat UI.</p>"
        "</div>",
        unsafe_allow_html=True,
    )

    st.write("---")

    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader("Ask a question")
        with st.form(key="query_form", clear_on_submit=True):
            query = st.text_input("Enter your algorithm question", placeholder="e.g. What is BFS?", label_visibility="collapsed")
            submit = st.form_submit_button("Send")

    with col2:
        st.subheader("Quick tips")
        st.markdown(
            "- Ask about BFS, DFS, A*, AO*, Hill Climbing, or Best First Search.\n"
            "- Use plain English questions."
        )

    if "history" not in st.session_state:
        st.session_state.history = []

    bot = AlgorithmChatbot()

    if submit and query.strip():
        answer = bot.handle_query(query)
        st.session_state.history.append(("You", query.strip()))
        st.session_state.history.append(("AlgoWiki AI", answer))

    # Display History
    if st.session_state.history:
        st.write("---")
        for speaker, message in st.session_state.history:
            if speaker == "You":
                # User text in black
                st.markdown(f"<p style='color: #000000;'><strong>You:</strong> {message}</p>", unsafe_allow_html=True)
            else:
                # Bot bubble with explicit black text
                st.markdown(
                    f"<div style='background:#eef2ff; border-left:4px solid #1f3c88; border-radius:12px; padding:16px; margin-bottom:12px; color: #000000;'>"
                    f"<strong style='color: #000000;'>{speaker}:</strong> {message}" 
                    f"</div>",
                    unsafe_allow_html=True,
                )

    # Sidebar Content
    st.sidebar.title("About")
    st.sidebar.info("This app uses Wikipedia summaries to answer algorithm questions.")
    st.sidebar.markdown("---")
    st.sidebar.write("**Example questions**")
    st.sidebar.write("- What is BFS?\n- Explain A*\n- How does hill climbing work?")

if __name__ == "__main__":
    main()
