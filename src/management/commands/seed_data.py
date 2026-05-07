from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from src.models import HeroSlide, GalleryItem, BlogPost


class Command(BaseCommand):
    help = 'Seeds the database with initial data for HeroSlide, GalleryItem, and BlogPost models'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting data seeding...'))
        
        # Seed Hero Slides
        self.seed_hero_slides()
        
        # Seed Gallery Items
        self.seed_gallery_items()
        
        # Seed Blog Posts
        self.seed_blog_posts()
        
        self.stdout.write(self.style.SUCCESS('✓ Data seeding completed successfully!'))

    def seed_hero_slides(self):
        self.stdout.write('Seeding Hero Slides...')
        
        hero_slides_data = [
            {
                'title': 'Hulegeb',
                'heading_part1': 'Weaving',
                'heading_part2': 'Dignity',
                'heading_part3': ', Crafting Independence',
                'description': "For over 70 years, Hulegeb has been led by and for Ethiopia's blind and physically disabled community — turning skill into steady, dignified livelihoods.",
                'image_url': 'https://i.postimg.cc/VvQRbrh9/L2A6687.jpg',
                'image_alt': 'Hulegeb artisans at work',
                'order': 1,
                'is_active': True
            },
            {
                'title': 'Hulegeb',
                'heading_part1': 'Empowering',
                'heading_part2': 'Communities',
                'heading_part3': ', Building Futures',
                'description': 'Through vocational training and sustainable employment, we create pathways to independence for people with disabilities.',
                'image_url': 'https://i.postimg.cc/2SsVYQLX/L2A6618.jpg',
                'image_alt': 'Training and rehabilitation center',
                'order': 2,
                'is_active': True
            },
            {
                'title': 'Hulegeb',
                'heading_part1': 'Traditional',
                'heading_part2': 'Crafts',
                'heading_part3': ', Modern Impact',
                'description': 'Hand-woven textiles, custom furniture, and quality products made by skilled artisans with disabilities.',
                'image_url': 'https://i.postimg.cc/SRHp9rhc/L2A5446.jpg',
                'image_alt': 'Artisan crafting products',
                'order': 3,
                'is_active': True
            }
        ]
        
        for data in hero_slides_data:
            slide, created = HeroSlide.objects.get_or_create(
                title=data['title'],
                heading_part1=data['heading_part1'],
                heading_part2=data['heading_part2'],
                defaults=data
            )
            if created:
                self.stdout.write(f'  ✓ Created: {slide}')
            else:
                self.stdout.write(f'  - Already exists: {slide}')

    def seed_gallery_items(self):
        self.stdout.write('Seeding Gallery Items...')
        
        gallery_items_data = [
            # Images
            {
                'title': 'Weaving Workshop',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKIp6fn.jpg',
                'alt_text': 'Artisans working on traditional looms',
                'order': 1,
                'is_active': True
            },
            {
                'title': 'Furniture Production',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKTRuYG.jpg',
                'alt_text': 'Craftsmen creating wooden furniture',
                'order': 2,
                'is_active': True
            },
            {
                'title': 'Training Session',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKu8fXV.jpg',
                'alt_text': 'Vocational training in progress',
                'order': 3,
                'is_active': True
            },
            {
                'title': 'Artisan at Work',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKu4fF2.jpg',
                'alt_text': 'Skilled artisan crafting products',
                'order': 4,
                'is_active': True
            },
            {
                'title': 'Hand-Woven Carpets',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKutxCF.jpg',
                'alt_text': 'Beautiful hand-woven carpets',
                'order': 5,
                'is_active': True
            },
            {
                'title': 'Textile Production',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKAHNJn.jpg',
                'alt_text': 'Eco-friendly fabric production',
                'order': 6,
                'is_active': True
            },
            {
                'title': 'Workshop Overview',
                'media_type': 'image',
                'image_url': 'https://i.postimg.cc/yN3JYd7J/L2A6101.jpg',
                'alt_text': 'Overview of production workshop',
                'order': 7,
                'is_active': True
            },
            {
                'title': 'Craftsmanship',
                'media_type': 'image',
                'image_url': 'https://i.postimg.cc/KjjZBjgF/L2A6116.jpg',
                'alt_text': 'Detailed craftsmanship work',
                'order': 8,
                'is_active': True
            },
            {
                'title': 'Community Impact',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKuzPpV.jpg',
                'alt_text': 'Community members working together',
                'order': 9,
                'is_active': True
            },
            {
                'title': 'Milling Services',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKu7EAJ.jpg',
                'alt_text': 'Community milling services in operation',
                'order': 10,
                'is_active': True
            },
            {
                'title': 'Advocacy Programs',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKulLqQ.jpg',
                'alt_text': 'Disability rights advocacy and awareness programs',
                'order': 11,
                'is_active': True
            },
            {
                'title': 'Artisan Production Floor',
                'media_type': 'image',
                'image_url': 'https://i.postimg.cc/VvQRbrh9/L2A6687.jpg',
                'alt_text': 'Busy production floor with multiple artisans',
                'order': 12,
                'is_active': True
            },
            {
                'title': 'Weaving Techniques',
                'media_type': 'image',
                'image_url': 'https://i.postimg.cc/2SsVYQLX/L2A6618.jpg',
                'alt_text': 'Close-up of traditional weaving techniques',
                'order': 13,
                'is_active': True
            },
            {
                'title': 'Finished Products Display',
                'media_type': 'image',
                'image_url': 'https://i.postimg.cc/SRHp9rhc/L2A5446.jpg',
                'alt_text': 'Display of finished handcrafted products',
                'order': 14,
                'is_active': True
            },
            {
                'title': 'Woodworking Workshop',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKu8fXV.jpg',
                'alt_text': 'Carpenters working on custom furniture pieces',
                'order': 15,
                'is_active': True
            },
            {
                'title': 'Quality Control',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKIp6fn.jpg',
                'alt_text': 'Quality inspection of finished products',
                'order': 16,
                'is_active': True
            },
            {
                'title': 'Team Collaboration',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKTRuYG.jpg',
                'alt_text': 'Artisans collaborating on a project',
                'order': 17,
                'is_active': True
            },
            {
                'title': 'Traditional Loom Work',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKu4fF2.jpg',
                'alt_text': 'Artisan working on traditional hand loom',
                'order': 18,
                'is_active': True
            },
            {
                'title': 'Product Packaging',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKutxCF.jpg',
                'alt_text': 'Careful packaging of handcrafted products',
                'order': 19,
                'is_active': True
            },
            {
                'title': 'Training New Artisans',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKAHNJn.jpg',
                'alt_text': 'Experienced artisan training new team members',
                'order': 20,
                'is_active': True
            },
            {
                'title': 'Brush Making Workshop',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKuzPpV.jpg',
                'alt_text': 'Production of household brushes and cleaning tools',
                'order': 21,
                'is_active': True
            },
            {
                'title': 'Carpet Weaving Detail',
                'media_type': 'image',
                'image_url': 'https://i.postimg.cc/yN3JYd7J/L2A6101.jpg',
                'alt_text': 'Intricate detail work on hand-woven carpet',
                'order': 22,
                'is_active': True
            },
            {
                'title': 'Workshop Facilities',
                'media_type': 'image',
                'image_url': 'https://i.postimg.cc/KjjZBjgF/L2A6116.jpg',
                'alt_text': 'Modern workshop facilities and equipment',
                'order': 23,
                'is_active': True
            },
            {
                'title': 'Artisan Pride',
                'media_type': 'image',
                'image_url': 'https://iili.io/qKu7EAJ.jpg',
                'alt_text': 'Artisan proudly displaying finished work',
                'order': 24,
                'is_active': True
            },
          
        ]
        
        for data in gallery_items_data:
            item, created = GalleryItem.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(f'  ✓ Created: {item}')
            else:
                self.stdout.write(f'  - Already exists: {item}')

    def seed_blog_posts(self):
        self.stdout.write('Seeding Blog Posts...')
        
        blog_posts_data = [
            {
                'title': 'Beyond Charity: How a Disabled-Led Model Builds True Independence',
                'slug': 'beyond-charity-disabled-led-model',
                'excerpt': 'Explore the power of empowerment over aid through Hulegeb\'s 70-year journey of creating sustainable livelihoods.',
                'content': '''For over seven decades, Hulegeb has pioneered a revolutionary approach to disability inclusion in Ethiopia. Rather than relying on charity or handouts, we've built a self-sustaining social enterprise that puts people with disabilities in the driver's seat.

Our model is simple but powerful: provide comprehensive vocational training, create dignified employment opportunities, and let skilled artisans earn their own living through quality craftsmanship. This approach transforms lives not through pity, but through respect and opportunity.

The results speak for themselves. Today, 85 individuals with visual and physical disabilities work at Hulegeb, producing hand-woven textiles, custom furniture, and household goods that compete in the open market. They're not charity cases—they're skilled professionals earning fair wages for quality work.

This disabled-led model proves that with the right support and opportunities, people with disabilities can be economically independent, socially integrated, and proud contributors to their communities. It's not about what we do for people—it's about what we enable them to do for themselves.''',
                'featured_image_url': 'https://i.postimg.cc/yN3JYd7J/L2A6101.jpg',
                'image_alt': 'Artisans working in the Hulegeb workshop',
                'author': 'Hulegeb Team',
                'published_date': date.today() - timedelta(days=3),
                'is_published': True,
                'is_featured': True,
                'meta_description': 'Discover how Hulegeb\'s disabled-led social enterprise model creates true independence through vocational training and dignified employment.'
            },
            {
                'title': 'Weaving Dignity: A Day in the Life of a Hulegeb Artisan',
                'slug': 'weaving-dignity-day-in-life',
                'excerpt': 'An intimate look at how skill, craft, and purpose come together on the production floor.',
                'content': '''The morning sun filters through the windows of Hulegeb's weaving workshop as Alemayehu settles at his loom. Blind since childhood, his hands move with practiced confidence across the threads, creating intricate patterns that will become beautiful carpets and textiles.

"People think I can't work because I can't see," Alemayehu says with a smile. "But my hands see everything they need to." He's been with Hulegeb for 15 years, starting as a trainee and now mentoring new artisans.

The workshop buzzes with activity. In one corner, carpenters craft custom furniture. In another, workers operate the community milling service. Each person has found their niche, their skill, their dignity through work.

What makes Hulegeb special isn't just the training or the jobs—it's the culture of respect and independence. Artisans aren't treated as charity recipients but as valued professionals. They earn competitive wages, have opportunities for advancement, and take pride in their craftsmanship.

"When I finish a carpet, I know it will go to someone's home," Alemayehu explains. "They chose it because it's beautiful and well-made, not because they feel sorry for me. That's dignity."

This is the daily reality at Hulegeb: skilled hands creating quality products, earning honest wages, and building independent lives. It's not a charity story—it's a success story.''',
                'featured_image_url': 'https://i.postimg.cc/KjjZBjgF/L2A6116.jpg',
                'image_alt': 'Artisan weaving at traditional loom',
                'author': 'Hulegeb Team',
                'published_date': date.today() - timedelta(days=7),
                'is_published': True,
                'is_featured': False,
                'meta_description': 'Follow a day in the life of Alemayehu, a blind artisan at Hulegeb, and discover how skill and dignity come together through meaningful work.'
            },
            {
                'title': 'From Trainee to Trainer: Stories of Transformation at Hulegeb',
                'slug': 'trainee-to-trainer-transformation',
                'excerpt': 'Personal journeys of individuals who learned a trade and now lead others toward self-reliance.',
                'content': '''Meseret remembers her first day at Hulegeb vividly. Newly disabled from an accident, she felt lost and uncertain about her future. "I thought my productive life was over," she recalls. "I couldn't imagine how I would support myself."

That was eight years ago. Today, Meseret is a senior trainer in Hulegeb's woodworking program, teaching new trainees the skills that transformed her own life. Her journey from uncertain trainee to confident trainer embodies Hulegeb's mission of empowerment through skill development.

The transformation isn't just about learning a trade—it's about rebuilding confidence and independence. "When you master a skill, when you create something with your own hands, when you earn your own money—that changes everything," Meseret explains.

She's not alone. Many of Hulegeb's current trainers and supervisors started as trainees themselves. This peer-to-peer model is powerful: who better to teach and inspire new trainees than someone who has walked the same path?

"I tell new trainees: I was where you are," Meseret says. "I know the doubts, the fears. But I also know what's possible. If I can do it, so can you."

These stories of transformation—from dependent to independent, from trainee to trainer, from uncertain to confident—are the heart of Hulegeb's impact. They prove that with the right support and opportunities, disability doesn't define limits—it's just one part of a person's story.''',
                'featured_image_url': 'https://iili.io/qKu8fXV.jpg',
                'image_alt': 'Trainer teaching woodworking skills',
                'author': 'Hulegeb Team',
                'published_date': date.today() - timedelta(days=10),
                'is_published': True,
                'is_featured': False,
                'meta_description': 'Read inspiring stories of Hulegeb trainees who became trainers, leading others on the path from dependency to independence.'
            },
            {
                'title': 'The Economics of Empowerment: How Social Enterprise Sustains Impact',
                'slug': 'economics-of-empowerment-social-enterprise',
                'excerpt': 'Understanding the business model that makes Hulegeb\'s mission sustainable for over 70 years.',
                'content': '''Hulegeb's longevity—over 70 years of continuous operation—isn't accidental. It's the result of a carefully balanced social enterprise model that generates revenue while creating social impact.

Unlike traditional charities that depend on donations, Hulegeb operates as a business. We produce and sell quality products: hand-woven carpets, custom furniture, household goods, and milling services. These sales generate revenue that funds operations, pays fair wages, and supports training programs.

This business approach has several advantages. First, it's sustainable—we're not dependent on the whims of donors or grant cycles. Second, it's dignified—our artisans are employees earning wages, not charity recipients. Third, it's market-driven—we must maintain quality and competitiveness, which drives continuous improvement.

But we're not just any business. As a social enterprise, profit isn't our primary goal—impact is. Revenue is reinvested into training programs, facility improvements, and expanding employment opportunities. We also maintain 28,287 square meters of endowed land for social purposes.

The model works because it aligns economic incentives with social mission. Quality products lead to sales, which fund wages and training, which develop skilled artisans, who produce quality products. It's a virtuous cycle of empowerment and sustainability.

This is the future of disability inclusion: not charity, but enterprise. Not handouts, but opportunities. Not pity, but respect. And it's been working for 70 years.''',
                'featured_image_url': 'https://iili.io/qKu4fF2.jpg',
                'image_alt': 'Hulegeb production facility',
                'author': 'Hulegeb Team',
                'published_date': date.today() - timedelta(days=14),
                'is_published': True,
                'is_featured': False,
                'meta_description': 'Learn how Hulegeb\'s social enterprise model creates sustainable impact through business principles and social mission.'
            },
            {
                'title': 'Traditional Crafts, Modern Markets: Bridging Heritage and Commerce',
                'slug': 'traditional-crafts-modern-markets',
                'excerpt': 'How Hulegeb preserves Ethiopian craft traditions while competing in contemporary markets.',
                'content': '''The hand looms at Hulegeb are the same type used in Ethiopia for centuries. The weaving techniques passed down through generations. Yet the products—vibrant carpets, elegant textiles, custom designs—compete successfully in modern markets.

This balance between tradition and innovation is central to Hulegeb's approach. We honor traditional Ethiopian craftsmanship while adapting to contemporary needs and aesthetics. It's not about choosing between heritage and commerce—it's about making heritage commercially viable.

Our artisans learn traditional techniques but also modern design principles. They work with time-honored tools but understand current market trends. The result is products that carry cultural authenticity while meeting modern standards of quality and design.

This approach benefits everyone. Customers get unique, handcrafted products with cultural significance. Artisans preserve valuable traditional skills while earning competitive wages. Ethiopian craft heritage remains alive and relevant rather than becoming a museum piece.

The furniture workshop exemplifies this balance. Using traditional joinery techniques and local materials, our carpenters create pieces that are both culturally rooted and contemporary in design. Each piece tells a story of Ethiopian craftsmanship while fitting seamlessly into modern homes and offices.

In a globalized economy dominated by mass production, there's growing appreciation for authentic, handcrafted goods. Hulegeb's products offer exactly that—genuine craftsmanship, cultural heritage, and the knowledge that your purchase supports dignified employment for people with disabilities.

Traditional crafts and modern markets aren't opposites—they're partners in creating sustainable livelihoods and preserving cultural heritage.''',
                'featured_image_url': 'https://iili.io/qKutxCF.jpg',
                'image_alt': 'Traditional hand-woven carpet',
                'author': 'Hulegeb Team',
                'published_date': date.today() - timedelta(days=18),
                'is_published': True,
                'is_featured': False,
                'meta_description': 'Discover how Hulegeb bridges Ethiopian craft traditions and modern markets, creating sustainable livelihoods through cultural heritage.'
            },
            {
                'title': 'Disability Rights and Economic Justice: The Hulegeb Approach',
                'slug': 'disability-rights-economic-justice',
                'excerpt': 'Why employment and economic independence are fundamental disability rights issues.',
                'content': '''Disability rights aren't just about accessibility ramps and anti-discrimination laws—though those are important. At their core, disability rights are about economic justice: the right to work, earn a living, and participate fully in economic life.

This is where Hulegeb's approach becomes radical. We don't just advocate for disability rights—we create the economic conditions that make those rights real. Employment isn't charity; it's a right. Fair wages aren't generosity; they're justice.

For too long, people with disabilities have been excluded from economic participation. Seen as unable to work, they've been relegated to dependency on family or charity. This exclusion isn't just economically damaging—it's a fundamental violation of human dignity and rights.

Hulegeb challenges this exclusion directly. By providing vocational training and creating employment opportunities, we assert that people with disabilities have the right and ability to be economically productive. By paying fair wages, we affirm that their work has real value. By operating as a business, we prove that disability inclusion makes economic sense.

This approach has ripple effects beyond our 85 employees. We demonstrate to other businesses that hiring people with disabilities is viable. We show families that their disabled members can be independent. We prove to society that disability doesn't mean inability.

Economic justice for people with disabilities requires more than good intentions—it requires structural change. It requires businesses willing to hire, training programs that develop real skills, and markets that value quality over prejudice.

Hulegeb has been doing this work for 70 years. We've proven it's possible. Now it's time for this approach to become the norm, not the exception. Disability rights are economic rights, and economic rights require economic opportunities.''',
                'featured_image_url': 'https://iili.io/qKuzPpV.jpg',
                'image_alt': 'Artisans working together',
                'author': 'Hulegeb Team',
                'published_date': date.today() - timedelta(days=21),
                'is_published': True,
                'is_featured': False,
                'meta_description': 'Explore how Hulegeb connects disability rights with economic justice through employment and fair wages for people with disabilities.'
            },
            {
    'title': 'Skill Over Sympathy: Why Training Changes Everything',
    'slug': 'skill-over-sympathy-training-changes-everything',
    'excerpt': 'Why vocational training is the most powerful tool for building independence among people with disabilities.',
    'content': '''At Hulegeb, the focus has always been on skills rather than sympathy. While charity may provide short-term relief, real independence comes from learning a trade and mastering a craft.

        For new trainees arriving at Hulegeb, the first lesson is often the most important: ability matters more than disability. Each trainee is introduced to practical vocational skills—from weaving and carpentry to milling and workshop operations.

        Training is hands-on and mentorship-driven. Experienced artisans guide trainees through each step of the process, ensuring they develop not only technical skills but also confidence.

        Over time, trainees discover something powerful: their work has value. A carpet woven with patience and precision becomes a product someone is willing to buy. A carefully crafted chair becomes part of someone's home.

        This realization changes everything. Instead of seeing themselves as dependent on support, trainees begin to see themselves as skilled workers capable of earning a living.

        At Hulegeb, training is not just about employment—it's about transforming identity from recipient to creator.''',
            'featured_image_url': 'https://iili.io/qKutxCF.jpg',
            'image_alt': 'Vocational training session at Hulegeb',
            'author': 'Hulegeb Team',
            'published_date': date.today() - timedelta(days=25),
            'is_published': True,
            'is_featured': False,
            'meta_description': 'Learn how vocational training empowers people with disabilities to build independence and meaningful careers at Hulegeb.'
        },
        {
            'title': 'Craftsmanship That Tells a Story',
            'slug': 'craftsmanship-that-tells-a-story',
            'excerpt': 'Every handmade product at Hulegeb carries the story of skill, perseverance, and dignity.',
            'content': '''Every product created at Hulegeb carries more than just material value—it carries a story.

        A hand-woven carpet may take days to complete. Each thread is carefully placed, each pattern formed with practiced hands. For the artisan who created it, the finished product represents dedication, patience, and pride.

        Customers often admire the beauty and durability of these handcrafted goods. What they may not immediately see is the deeper story behind them: the story of individuals who overcame barriers to become skilled professionals.

        Craftsmanship at Hulegeb reflects the belief that quality speaks louder than stereotypes. When someone buys a piece of furniture or a woven carpet from Hulegeb, they are choosing a product that stands on its own merit.

        This is the power of craftsmanship—it allows skill to speak for itself.

        For the artisans, every completed piece is proof that their abilities define them far more than their disabilities ever could.''',
            'featured_image_url': 'https://iili.io/qKu8fXV.jpg',
            'image_alt': 'Handcrafted carpet made by Hulegeb artisans',
            'author': 'Hulegeb Team',
            'published_date': date.today() - timedelta(days=30),
            'is_published': True,
            'is_featured': False,
            'meta_description': 'Discover the stories behind the handcrafted products made by skilled artisans at Hulegeb.'
        },
        {
            'title': 'Community Impact: Beyond the Workshop Walls',
            'slug': 'community-impact-beyond-workshop-walls',
            'excerpt': 'How Hulegeb’s work benefits families, communities, and the broader economy.',
            'content': '''The impact of Hulegeb extends far beyond the walls of its workshops.

        When a person with a disability gains stable employment, the benefits ripple outward. Families experience greater financial security. Communities gain skilled workers and entrepreneurs. Local markets benefit from quality products and services.

        For many artisans, employment at Hulegeb allows them to support relatives, contribute to household expenses, and participate fully in community life.

        The social impact is just as significant as the economic one. As communities witness people with disabilities working, producing, and earning wages, long-standing stereotypes begin to fade.

        This visibility helps change attitudes about disability. Instead of seeing limitations, people begin to see capability and contribution.

        Through employment, training, and enterprise, Hulegeb demonstrates that inclusion is not only the right thing to do—it strengthens communities as a whole.''',
            'featured_image_url': 'https://i.postimg.cc/yN3JYd7J/L2A6101.jpg',
            'image_alt': 'Community members interacting with Hulegeb artisans',
            'author': 'Hulegeb Team',
            'published_date': date.today() - timedelta(days=35),
            'is_published': True,
            'is_featured': False,
            'meta_description': 'Explore how Hulegeb creates positive economic and social impact for families and communities.'
        },
        {
            'title': 'Redefining Ability Through Work',
            'slug': 'redefining-ability-through-work',
            'excerpt': 'Employment changes how society views disability—and how individuals view themselves.',
            'content': '''Work has the power to transform not only lives but also perceptions.

        At Hulegeb, artisans with visual and physical disabilities demonstrate daily that ability is not defined by physical limitations. Through craftsmanship, discipline, and dedication, they challenge the assumptions that often surround disability.

        Employment offers more than income. It provides purpose, routine, and the confidence that comes from contributing meaningfully to society.

        When customers purchase a Hulegeb product, they often become part of a larger story—one where talent and determination overcome barriers.

        For the artisans themselves, the transformation is deeply personal. Work brings independence, pride, and a renewed sense of identity.

        By redefining ability through meaningful work, Hulegeb continues to prove that inclusion benefits everyone.''',
            'featured_image_url': 'https://iili.io/qKuzPpV.jpg',
            'image_alt': 'Artisans collaborating in workshop',
            'author': 'Hulegeb Team',
            'published_date': date.today() - timedelta(days=40),
            'is_published': True,
            'is_featured': False,
            'meta_description': 'See how employment and craftsmanship help redefine ability and promote inclusion.'
        }
        ]
        
        for data in blog_posts_data:
            post, created = BlogPost.objects.get_or_create(
                slug=data['slug'],
                defaults=data
            )
            if created:
                self.stdout.write(f'  ✓ Created: {post.title}')
            else:
                self.stdout.write(f'  - Already exists: {post.title}')
