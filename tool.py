import requests
import json
from typing import List, Dict, Any
from langchain.agents import Tool
from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class AICompetitiveResearch:
    def __init__(self, api_key: str, groq_api_key: str):
        """
        Initialize AI competitive research tool with agent-based research
        """
        self.serper_api_key = api_key
        
        # Single LLM for all tasks
        self.llm = ChatGroq(
            temperature=0.1,
            groq_api_key=groq_api_key,
            model_name="llama-3.3-70b-versatile"
        )
        
        # Create web search tool
        self.tools = [
            Tool(
                name="web_search",
                func=self.web_search,
                description="Conduct targeted web searches for AI offerings and case studies"
            )
        ]
        
        # Research prompt with agent-specific structure
        self.research_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert AI research analyst. Your task is to comprehensively document:
            1. Detailed AI offerings of the company
            2. Specific case studies and client implementations (mention client names if found)
            3. Technological innovations and unique AI solutions
            
            Use available tools to gather information. Provide clear, structured, and verifiable insights."""),
            MessagesPlaceholder(variable_name="chat_history", optional=True),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        
        # Create research agent
        self.research_agent = create_openai_tools_agent(
            self.llm, 
            self.tools, 
            self.research_prompt
        )
        self.research_executor = AgentExecutor(
            agent=self.research_agent, 
            tools=self.tools, 
            verbose=True
        )

    def web_search(self, query: str) -> str:
        """
        Perform a targeted web search
        """
        url = "https://google.serper.dev/search"
        payload = json.dumps({
            "q": query + " AI offerings case studies",
            "num": 7
        })
        headers = {
            'X-API-KEY': self.serper_api_key,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text

    def extract_sources(self, search_results: str) -> List[Dict[str, str]]:
        """
        Extract unique sources from search results
        """
        try:
            results = json.loads(search_results)
            sources = []
            source_links = set()
            
            if 'organic' in results:
                for result in results['organic']:
                    link = result.get('link', '')
                    if link and link not in source_links:
                        sources.append({
                            'title': result.get('title', 'Untitled'),
                            'link': link,
                            'snippet': result.get('snippet', '')
                        })
                        source_links.add(link)
            
            return sources
        except Exception as e:
            print(f"Error extracting sources: {e}")
            return []

    def research_companies(self, companies: List[str], parent_company: str) -> Dict[str, Any]:
        """
        Comprehensive agent-based research on AI offerings
        """
        research_results = {}
        
        # Research all companies including parent company
        all_companies = companies + [parent_company]
        for company in all_companies:
            if not company:
                continue
            
            # Perform web search
            search_query = f"{company} AI offerings technology case studies client projects"
            search_results = self.web_search(search_query)
            sources = self.extract_sources(search_results)
            
            # Conduct detailed AI offerings research using agent
            research = self.research_executor.invoke({
                "input": f"Comprehensive analysis of {company}'s AI offerings, technological capabilities, and notable case studies. Provide detailed insights into their AI implementations."
            })
            
            research_results[company] = {
                'ai_offerings': research.get('output', 'No detailed AI offerings found'),
                'sources': sources
            }
        
        # Direct LLM-based comparison
        comparison_prompt = f"""Compare the AI capabilities of {', '.join(companies)} in relation to {parent_company}. 
        Analyze:
        1. Technological strengths and unique offerings
        2. Comparative advantages
        3. Potential competitive positioning
        Focus specifically on how the other companies compare to {parent_company}."""
        
        comparison_result = self.llm.invoke(comparison_prompt)
        research_results['comparative_analysis'] = comparison_result.content
        
        return research_results

    def generate_markdown_report(self, research_data: Dict[str, Any]) -> str:
        """
        Generate a comprehensive markdown report
        """
        report = "# AI Offerings and Case Studies Competitive Research Report\n\n"
        
        # Company-specific sections
        for company, data in research_data.items():
            if company != 'comparative_analysis':
                report += f"## {company} AI Offerings\n\n"
                report += f"{data['ai_offerings']}\n\n"
                
                report += "### Research Sources:\n"
                for source in data.get('sources', []):
                    report += f"- **{source['title']}**: {source['link']}\n"
                report += "\n"
        
        # Comparative analysis section
        report += "## Comparative Analysis\n\n"
        report += f"{research_data.get('comparative_analysis', 'No comparative analysis available')}\n"
        
        return report
    
    def export_markdown(self, research_data: Dict[str, Any], filename: str = 'ai_competitive_research.md'):
        """
        Export research findings to a Markdown file
        
        :param research_data: Comprehensive research results
        :param filename: Output filename for the Markdown document
        """
        report = self.generate_markdown_report(research_data)
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"Markdown report exported successfully to {filename}")
        except IOError as e:
            print(f"Error exporting Markdown file: {e}")
    

def main():
    # Replace with actual API keys
    SERPER_API_KEY = ''
    GROQ_API_KEY = ''
    
    # Initialize research tool
    researcher = AICompetitiveResearch(SERPER_API_KEY, GROQ_API_KEY)
    
    # Conduct research
    research_results = researcher.research_companies(
        companies=['org1', 'org1'],
        parent_company='parent_org(optional)'
    )
    
    # Generate markdown report
    
    # report = researcher.generate_markdown_report(research_results)
    # print(report)
    researcher.export_markdown(research_results)

if __name__ == "__main__":
    main()