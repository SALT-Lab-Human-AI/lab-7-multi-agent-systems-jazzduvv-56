"""
Simplified AutoGen Demo - Interview Platform Product Planning

This is a lightweight version for quick testing and understanding the workflow.
It demonstrates multi-agent collaboration by having each agent generate responses.
"""

from datetime import datetime
from config import Config, WorkflowConfig, AgentConfig
import json

# Try to import OpenAI client
try:
    from openai import OpenAI
except ImportError:
    print("ERROR: OpenAI client is not installed!")
    print("Please run: pip install -r ../requirements.txt")
    exit(1)


class SimpleInterviewPlatformWorkflow:
    """Simplified workflow for interview platform planning"""

    def __init__(self):
        """Initialize the workflow"""
        if not Config.validate_setup():
            print("ERROR: Configuration validation failed!")
            exit(1)

        self.client = OpenAI(api_key=Config.API_KEY, base_url=Config.API_BASE)
        self.outputs = {}
        self.model = Config.OPENAI_MODEL

    def run(self):
        """Execute the complete workflow"""
        print("\n" + "="*80)
        print("AUTOGEN INTERVIEW PLATFORM WORKFLOW - SIMPLIFIED DEMO")
        print("="*80)
        print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Model: {self.model}\n")

        # Phase 1: Research
        self.phase_research()

        # Phase 2: Analysis
        self.phase_analysis()

        # Phase 3: Blueprint
        self.phase_blueprint()

        # Phase 4: Review
        self.phase_review()

        # Phase 5: Marketing
        self.phase_marketing()

        # Summary
        self.print_summary()

    def phase_research(self):
        """Phase 1: Market Research"""
        print("\n" + "="*80)
        print("PHASE 1: MARKET RESEARCH")
        print("="*80)
        agent_config = AgentConfig.get_agent_config("research")
        print(f"[{agent_config['name']} ({agent_config['role']}) is analyzing the market...]")

        system_prompt = f"""You are a {agent_config['role']}. Provide a brief analysis of
3 competitors in AI interview platforms (HireVue, Pymetrics, Codility).
List their key features and identify market gaps in 150 words."""

        user_message = "Analyze the current market for AI-powered interview platforms."

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["research"] = response.choices[0].message.content
        print(f"\n[{agent_config['name']} Output]")
        print(self.outputs["research"])

    def phase_analysis(self):
        """Phase 2: Opportunity Analysis"""
        print("\n" + "="*80)
        print("PHASE 2: OPPORTUNITY ANALYSIS")
        print("="*80)
        agent_config = AgentConfig.get_agent_config("analysis")
        print(f"[{agent_config['name']} ({agent_config['role']}) is identifying opportunities...]")

        system_prompt = f"""You are a {agent_config['role']}. Based on the market research provided,
identify 3 key market opportunities or gaps for a new AI interview platform.
Be concise in 150 words."""

        user_message = f"""Market research findings:
{self.outputs['research']}

Now identify market opportunities and gaps."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["analysis"] = response.choices[0].message.content
        print(f"\n[{agent_config['name']} Output]")
        print(self.outputs["analysis"])

    def phase_blueprint(self):
        """Phase 3: Product Blueprint"""
        print("\n" + "="*80)
        print("PHASE 3: PRODUCT BLUEPRINT")
        print("="*80)
        agent_config = AgentConfig.get_agent_config("blueprint")
        print(f"[{agent_config['name']} ({agent_config['role']}) is designing the product...]")

        system_prompt = f"""You are a {agent_config['role']}. Based on the market analysis and opportunities,
create a brief product blueprint including:
- Key features (3-5)
- User journey (2-3 steps)
Keep it concise - 150 words."""

        user_message = f"""Market Analysis:
{self.outputs['analysis']}

Create a product blueprint for our platform."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["blueprint"] = response.choices[0].message.content
        print(f"\n[{agent_config['name']} Output]")
        print(self.outputs["blueprint"])

    def phase_review(self):
        """Phase 4: Strategic Review"""
        print("\n" + "="*80)
        print("PHASE 4: STRATEGIC REVIEW")
        print("="*80)
        agent_config = AgentConfig.get_agent_config("reviewer")
        print(f"[{agent_config['name']} ({agent_config['role']}) is providing recommendations...]")

        system_prompt = f"""You are a {agent_config['role']}. Review the product blueprint
and provide 3 strategic recommendations for success.
Be concise - 150 words."""

        user_message = f"""Product Blueprint:
{self.outputs['blueprint']}

Provide strategic review and recommendations."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["review"] = response.choices[0].message.content
        print(f"\n[{agent_config['name']} Output]")
        print(self.outputs["review"])

    def phase_marketing(self):
        """Phase 5: Marketing Strategy"""
        print("\n" + "="*80)
        print("PHASE 5: MARKETING STRATEGY")
        print("="*80)
        agent_config = AgentConfig.get_agent_config("marketing")
        print(f"[{agent_config['name']} ({agent_config['role']}) is developing marketing strategy...]")

        system_prompt = f"""You are a {agent_config['role']}. Based on the product blueprint and strategic recommendations,
create a comprehensive go-to-market strategy including:
- Target customer segments (2-3)
- Marketing channels and tactics
- Pricing strategy
- Launch timeline
Keep it concise - 150 words."""

        user_message = f"""Product Blueprint:
{self.outputs['blueprint']}

Strategic Recommendations:
{self.outputs['review']}

Develop a comprehensive marketing and launch strategy."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["marketing"] = response.choices[0].message.content
        print(f"\n[{agent_config['name']} Output]")
        print(self.outputs["marketing"])

    def print_summary(self):
        """Print final summary"""
        print("\n" + "="*80)
        print("FINAL SUMMARY")
        print("="*80)

        print("""
This workflow demonstrated a 5-agent collaboration:
1. {0} ({1}) - Analyzed the market
2. {2} ({3}) - Identified opportunities
3. {4} ({5}) - Designed the product
4. {6} ({7}) - Provided strategic recommendations
5. {8} ({9}) - Developed marketing strategy

Each agent received context from the previous agent's output,
demonstrating the sequential workflow pattern of AutoGen.
""".format(
    AgentConfig.RESEARCH_AGENT['name'], AgentConfig.RESEARCH_AGENT['role'],
    AgentConfig.ANALYSIS_AGENT['name'], AgentConfig.ANALYSIS_AGENT['role'],
    AgentConfig.BLUEPRINT_AGENT['name'], AgentConfig.BLUEPRINT_AGENT['role'],
    AgentConfig.REVIEWER_AGENT['name'], AgentConfig.REVIEWER_AGENT['role'],
    AgentConfig.MARKETING_AGENT['name'], AgentConfig.MARKETING_AGENT['role']
))

        # Print full results
        print("\n" + "="*80)
        print("FULL RESULTS - ALL PHASES")
        print("="*80)
        
        print("\n" + "-"*80)
        print("PHASE 1: MARKET RESEARCH (Full Output)")
        print("-"*80)
        print(self.outputs["research"])
        
        print("\n" + "-"*80)
        print("PHASE 2: OPPORTUNITY ANALYSIS (Full Output)")
        print("-"*80)
        print(self.outputs["analysis"])
        
        print("\n" + "-"*80)
        print("PHASE 3: PRODUCT BLUEPRINT (Full Output)")
        print("-"*80)
        print(self.outputs["blueprint"])
        
        print("\n" + "-"*80)
        print("PHASE 4: STRATEGIC REVIEW (Full Output)")
        print("-"*80)
        print(self.outputs["review"])
        
        print("\n" + "-"*80)
        print("PHASE 5: MARKETING STRATEGY (Full Output)")
        print("-"*80)
        print(self.outputs["marketing"])

        # Save to file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"workflow_outputs_{timestamp}.txt"
        with open(output_file, 'w') as f:
            f.write("="*80 + "\n")
            f.write("AUTOGEN INTERVIEW PLATFORM WORKFLOW - FULL RESULTS\n")
            f.write("="*80 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Model: {self.model}\n\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 1: MARKET RESEARCH\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["research"] + "\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 2: OPPORTUNITY ANALYSIS\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["analysis"] + "\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 3: PRODUCT BLUEPRINT\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["blueprint"] + "\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 4: STRATEGIC REVIEW\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["review"] + "\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 5: MARKETING STRATEGY\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["marketing"] + "\n")
        
        print(f"\n💾 Full results saved to: {output_file}")

        print(f"\nEnd Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80)


if __name__ == "__main__":
    try:
        workflow = SimpleInterviewPlatformWorkflow()
        workflow.run()
        print("\n✅ Workflow completed successfully!")
    except Exception as e:
        print(f"\n❌ Error during workflow execution: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Verify OPENAI_API_KEY is set in parent directory .env (../.env)")
        print("2. Check your API key has sufficient credits")
        print("3. Verify internet connection")
        print("4. Ensure config.py can access shared_config from parent directory")
        print("5. Check OpenAI API status at https://status.openai.com")
        import traceback
        traceback.print_exc()
