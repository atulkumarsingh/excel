"""
Rebuild gallery.html main content:
- Keep header + hero (lines before <main>) unchanged
- Replace <main>...</main> + scripts with new Marriott-style layout
"""
HERO_END_MARKER = '<main id="main">'

NEW_MAIN = '''    <main id="main">

        <!-- ======= Property Filter Bar ======= -->
        <div class="gl-filter-section">
            <div class="gl-property-bar" role="tablist" aria-label="Filter by property">
                <button class="gl-prop-btn active" data-prop="all" role="tab" aria-selected="true">All Properties</button>
                <button class="gl-prop-btn" data-prop="la-perle" role="tab">La Perle River Resort</button>
                <button class="gl-prop-btn" data-prop="banyan" role="tab">The Banyan Retreat</button>
                <button class="gl-prop-btn" data-prop="excel-corbett" role="tab">Excel – Jim Corbett</button>
                <button class="gl-prop-btn" data-prop="excel-nainital" role="tab">Excel – Nainital</button>
                <button class="gl-prop-btn" data-prop="excel-bhimtal" role="tab">Excel – Bhimtal</button>
                <button class="gl-prop-btn" data-prop="mangobloom" role="tab">Mangobloom Resort</button>
            </div>
            <div class="gl-cat-bar" role="tablist" aria-label="Filter by category">
                <button class="gl-cat-btn active" data-cat="all">All</button>
                <button class="gl-cat-btn" data-cat="property">Property</button>
                <button class="gl-cat-btn" data-cat="rooms">Rooms &amp; Suites</button>
                <button class="gl-cat-btn" data-cat="dining">Dining</button>
                <button class="gl-cat-btn" data-cat="experiences">Experiences</button>
                <button class="gl-cat-btn" data-cat="events">Events</button>
            </div>
        </div>

        <!-- ======= Gallery Grid ======= -->
        <section class="gl-section">
            <div class="gl-count-row"><span id="glCount">Loading photos…</span></div>
            <div class="gl-empty" id="glEmpty"><p>No photos found.<br>Please try a different filter.</p></div>

            <!-- ===== LA PERLE RIVER RESORT ===== -->
            <div class="gl-prop-section" data-section="la-perle">
                <div class="gl-section-header">
                    <div class="gl-section-divider"></div>
                    <span class="gl-section-title">La Perle River Resort, Jim Corbett</span>
                    <div class="gl-section-divider-right"></div>
                </div>
                <div class="gl-tile-grid">
                    <!-- Row A: 3 equal tiles -->
                    <div class="gl-tile" data-prop="la-perle" data-cat="property" data-title="La Perle River Resort" data-caption="La Perle River Resort, Jim Corbett">
                        <img src="assets/img/LCP-LaPerle01.jpg" alt="La Perle River Resort" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>La Perle River Resort</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="la-perle" data-cat="property" data-title="La Perle Gallery" data-caption="La Perle River Resort">
                        <img src="assets/img/LCP-LaPerle03.jpg" alt="La Perle Resort" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>La Perle River Resort</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="la-perle" data-cat="property" data-title="La Perle Gallery" data-caption="La Perle River Resort">
                        <img src="assets/img/LCP-LaPerle04.jpg" alt="La Perle Resort" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>La Perle River Resort</h6><span>Property</span></div></div>
                    </div>
                    <!-- Row B: featured wide + stacked pair -->
                    <div class="gl-tile featured" data-prop="la-perle" data-cat="experiences" data-title="Riverside Deck" data-caption="La Perle River Resort – Riverside Deck">
                        <img src="assets/img/RiversideDeck.png" alt="Riverside Deck" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Riverside Deck</h6><span>Experiences</span></div></div>
                    </div>
                    <div class="gl-tile-stack">
                        <div class="gl-tile" data-prop="la-perle" data-cat="rooms" data-title="Leopards Lair Suite" data-caption="La Perle River Resort – Leopards Lair">
                            <img src="assets/img/LeopardsLair.jpg" alt="Leopards Lair" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Leopards Lair Suite</h6><span>Rooms &amp; Suites</span></div></div>
                        </div>
                        <div class="gl-tile" data-prop="la-perle" data-cat="rooms" data-title="Elephants Park Premium" data-caption="La Perle River Resort – Elephants Park">
                            <img src="assets/img/ElephantsPark.jpg" alt="Elephants Park" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Elephants Park Premium</h6><span>Rooms &amp; Suites</span></div></div>
                        </div>
                    </div>
                    <!-- Row C: 3 equal tiles -->
                    <div class="gl-tile" data-prop="la-perle" data-cat="rooms" data-title="Elephant Park Room" data-caption="La Perle River Resort – Elephant Park Room">
                        <img src="assets/img/ElephantParkRoom.jpg" alt="Elephant Park Room" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Elephant Park Room</h6><span>Rooms &amp; Suites</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="la-perle" data-cat="rooms" data-title="Jungle Suite River View" data-caption="La Perle River Resort – Jungle Suite">
                        <img src="assets/img/JungleSuite.jpg" alt="Jungle Suite" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Jungle Suite River View</h6><span>Rooms &amp; Suites</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="la-perle" data-cat="dining" data-title="Dine Under The Stars" data-caption="La Perle River Resort – Dining">
                        <img src="assets/img/LaPerleDIningExperience.png" alt="Dining" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Dine Under The Stars</h6><span>Dining</span></div></div>
                    </div>
                    <!-- Row D: stacked + featured -->
                    <div class="gl-tile-stack">
                        <div class="gl-tile" data-prop="la-perle" data-cat="events" data-title="Special Moments" data-caption="La Perle River Resort – Events">
                            <img src="assets/img/LaPerle1.png" alt="Special Moments" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Special Moments</h6><span>Events</span></div></div>
                        </div>
                        <div class="gl-tile" data-prop="la-perle" data-cat="events" data-title="La Perle Celebrations" data-caption="La Perle River Resort – Celebrations">
                            <img src="assets/img/LaPerle2.png" alt="La Perle Celebrations" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>La Perle Celebrations</h6><span>Events</span></div></div>
                        </div>
                    </div>
                    <div class="gl-tile featured" data-prop="la-perle" data-cat="experiences" data-title="Jungle Safari" data-caption="La Perle River Resort – Jungle Safari">
                        <img src="assets/img/JungleSafari.png" alt="Jungle Safari" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Jungle Safari</h6><span>Experiences</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="la-perle" data-cat="dining" data-title="Let's Dine Together" data-caption="La Perle River Resort – Restaurant">
                        <img src="assets/img/slickslider/letsdine25.jpg" alt="Dining" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Let's Dine Together</h6><span>Dining</span></div></div>
                    </div>
                </div>
            </div>

            <!-- ===== THE BANYAN RETREAT ===== -->
            <div class="gl-prop-section" data-section="banyan">
                <div class="gl-section-header">
                    <div class="gl-section-divider"></div>
                    <span class="gl-section-title">The Banyan Retreat, Jim Corbett</span>
                    <div class="gl-section-divider-right"></div>
                </div>
                <div class="gl-tile-grid">
                    <!-- Row A: 3 equal -->
                    <div class="gl-tile" data-prop="banyan" data-cat="property" data-title="The Banyan Retreat" data-caption="The Banyan Retreat, Jim Corbett">
                        <img src="assets/img/Banyan-Retreat.webp" alt="The Banyan Retreat" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>The Banyan Retreat</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="banyan" data-cat="property" data-title="Banyan Dome" data-caption="The Banyan Retreat – Dome">
                        <img src="assets/img/BanyanDome.jpg" alt="Banyan Dome" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Banyan Dome</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="banyan" data-cat="property" data-title="La Perle &amp; Banyan" data-caption="The Banyan Retreat – Gallery">
                        <img src="assets/img/LCP-Banyan01.jpg" alt="Banyan Gallery" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>The Banyan Retreat</h6><span>Property</span></div></div>
                    </div>
                    <!-- Row B: featured + stack -->
                    <div class="gl-tile featured" data-prop="banyan" data-cat="events" data-title="Banyan Lawns" data-caption="The Banyan Retreat – Event Lawns">
                        <img src="assets/img/BanyanLawns.jpg" alt="Banyan Lawns" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Banyan Lawns</h6><span>Events</span></div></div>
                    </div>
                    <div class="gl-tile-stack">
                        <div class="gl-tile" data-prop="banyan" data-cat="rooms" data-title="Banyan Rooms" data-caption="The Banyan Retreat – Rooms">
                            <img src="assets/img/BanyanRooms1.jpg" alt="Banyan Rooms" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Banyan Rooms</h6><span>Rooms &amp; Suites</span></div></div>
                        </div>
                        <div class="gl-tile" data-prop="banyan" data-cat="rooms" data-title="Deluxe Rooms" data-caption="The Banyan Retreat – Deluxe Rooms">
                            <img src="assets/img/BanyanRooms2.jpg" alt="Banyan Deluxe" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Deluxe Rooms</h6><span>Rooms &amp; Suites</span></div></div>
                        </div>
                    </div>
                    <!-- Row C: 3 equal -->
                    <div class="gl-tile" data-prop="banyan" data-cat="rooms" data-title="Premium Rooms" data-caption="The Banyan Retreat – Premium Rooms">
                        <img src="assets/img/BanyanRooms3.jpg" alt="Banyan Premium" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Premium Rooms</h6><span>Rooms &amp; Suites</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="banyan" data-cat="experiences" data-title="Adventure Ziplining" data-caption="The Banyan Retreat – Ziplining">
                        <img src="assets/img/BanyanZiplining.png" alt="Ziplining" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Adventure Ziplining</h6><span>Experiences</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="banyan" data-cat="experiences" data-title="Kids Play Area" data-caption="The Banyan Retreat – Kids Play Area">
                        <img src="assets/img/BanyanKidsPlayArea.png" alt="Kids Play Area" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Kids Play Area</h6><span>Experiences</span></div></div>
                    </div>
                    <!-- Row D: stack + featured -->
                    <div class="gl-tile-stack">
                        <div class="gl-tile" data-prop="banyan" data-cat="experiences" data-title="Bonfire Setting" data-caption="The Banyan Retreat – Bonfire">
                            <img src="assets/img/Bonfire.jpg" alt="Bonfire" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Bonfire Setting</h6><span>Experiences</span></div></div>
                        </div>
                        <div class="gl-tile" data-prop="banyan" data-cat="dining" data-title="Culinary Warmth" data-caption="The Banyan Retreat – Restaurant">
                            <img src="assets/img/slickslider/letsdine2.jpg" alt="Dining" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Culinary Warmth</h6><span>Dining</span></div></div>
                        </div>
                    </div>
                    <div class="gl-tile featured" data-prop="banyan" data-cat="rooms" data-title="Banyan Suite" data-caption="The Banyan Retreat – Suite">
                        <img src="assets/img/BanyanRooms4.jpg" alt="Banyan Suite" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Banyan Suite</h6><span>Rooms &amp; Suites</span></div></div>
                    </div>
                </div>
            </div>

            <!-- ===== EXCEL HOTELS – JIM CORBETT ===== -->
            <div class="gl-prop-section" data-section="excel-corbett">
                <div class="gl-section-header">
                    <div class="gl-section-divider"></div>
                    <span class="gl-section-title">Excel Hotels &amp; Resorts, Jim Corbett</span>
                    <div class="gl-section-divider-right"></div>
                </div>
                <div class="gl-tile-grid">
                    <div class="gl-tile" data-prop="excel-corbett" data-cat="property" data-title="Excel Hotels, Jim Corbett" data-caption="Excel Hotels &amp; Resorts, Jim Corbett">
                        <img src="assets/img/Excel-Corbett.webp" alt="Excel Corbett" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Excel Hotels, Jim Corbett</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="excel-corbett" data-cat="property" data-title="Excel Corbett Gallery" data-caption="Excel Hotels &amp; Resorts, Jim Corbett">
                        <img src="assets/img/Kotabagh-Gallery1.png" alt="Kotabagh Gallery" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Excel – Jim Corbett</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="excel-corbett" data-cat="property" data-title="Excel Corbett Gallery" data-caption="Excel Hotels &amp; Resorts, Jim Corbett">
                        <img src="assets/img/Kotabagh-Gallery2.png" alt="Kotabagh Gallery" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Excel – Jim Corbett</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile featured" data-prop="excel-corbett" data-cat="property" data-title="Kotabagh Gallery" data-caption="Excel Hotels – Kotabagh">
                        <img src="assets/img/Kotabagh-Gallery3.png" alt="Kotabagh Gallery" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Excel – Jim Corbett</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile-stack">
                        <div class="gl-tile" data-prop="excel-corbett" data-cat="rooms" data-title="Kotabagh Rooms" data-caption="Excel Hotels – Rooms">
                            <img src="assets/img/Kotabagh Rooms1.jpg" alt="Kotabagh Rooms" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Kotabagh Rooms</h6><span>Rooms &amp; Suites</span></div></div>
                        </div>
                        <div class="gl-tile" data-prop="excel-corbett" data-cat="rooms" data-title="Kotabagh Deluxe" data-caption="Excel Hotels – Deluxe Rooms">
                            <img src="assets/img/Kotabagh Rooms2.jpg" alt="Kotabagh Deluxe" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Deluxe Rooms</h6><span>Rooms &amp; Suites</span></div></div>
                        </div>
                    </div>
                    <div class="gl-tile" data-prop="excel-corbett" data-cat="events" data-title="Conference Hall" data-caption="Excel Hotels – Conference Hall">
                        <img src="assets/img/ConferenceHall.jpg" alt="Conference Hall" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Conference Hall</h6><span>Events</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="excel-corbett" data-cat="events" data-title="Poolside Celebrations" data-caption="Excel Hotels – Pool Events">
                        <img src="assets/img/PoolSide.jpg" alt="Poolside" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Poolside Celebrations</h6><span>Events</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="excel-corbett" data-cat="property" data-title="Kotabagh Gallery" data-caption="Excel Hotels – Gallery">
                        <img src="assets/img/Kotabagh-Gallery4.png" alt="Kotabagh Gallery" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Excel – Jim Corbett</h6><span>Property</span></div></div>
                    </div>
                </div>
            </div>

            <!-- ===== EXCEL HOTELS – NAINITAL ===== -->
            <div class="gl-prop-section" data-section="excel-nainital">
                <div class="gl-section-header">
                    <div class="gl-section-divider"></div>
                    <span class="gl-section-title">Excel Hotels &amp; Resorts, Nainital</span>
                    <div class="gl-section-divider-right"></div>
                </div>
                <div class="gl-tile-grid">
                    <div class="gl-tile" data-prop="excel-nainital" data-cat="property" data-title="Excel Nainital" data-caption="Excel Hotels &amp; Resorts, Nainital">
                        <img src="assets/img/egallery1.jpg" alt="Excel Nainital" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Excel Hotels, Nainital</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="excel-nainital" data-cat="property" data-title="Excel Nainital Gallery" data-caption="Excel Hotels &amp; Resorts, Nainital">
                        <img src="assets/img/egallery2.jpg" alt="Excel Nainital Gallery" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Excel Hotels, Nainital</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="excel-nainital" data-cat="rooms" data-title="Nainital Rooms" data-caption="Excel Hotels Nainital – Rooms">
                        <img src="assets/img/egallery3.jpg" alt="Nainital Rooms" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Nainital Rooms</h6><span>Rooms &amp; Suites</span></div></div>
                    </div>
                    <div class="gl-tile featured" data-prop="excel-nainital" data-cat="experiences" data-title="Nainital Experiences" data-caption="Excel Hotels Nainital – Experiences">
                        <img src="assets/img/egallery4.jpg" alt="Nainital Experiences" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Nainital Experiences</h6><span>Experiences</span></div></div>
                    </div>
                    <div class="gl-tile-stack">
                        <div class="gl-tile" data-prop="excel-nainital" data-cat="property" data-title="Nainital Scenic" data-caption="Excel Hotels Nainital – Scenic Views">
                            <img src="assets/img/egallery5.jpg" alt="Nainital Scenic" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Nainital Scenic Views</h6><span>Property</span></div></div>
                        </div>
                        <div class="gl-tile" data-prop="excel-nainital" data-cat="property" data-title="Nainital Gallery" data-caption="Excel Hotels Nainital – Gallery">
                            <img src="assets/img/egallery10.jpg" alt="Nainital Gallery" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Nainital Gallery</h6><span>Property</span></div></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ===== EXCEL HOTELS – BHIMTAL ===== -->
            <div class="gl-prop-section" data-section="excel-bhimtal">
                <div class="gl-section-header">
                    <div class="gl-section-divider"></div>
                    <span class="gl-section-title">Excel Hotels &amp; Resorts, Bhimtal</span>
                    <div class="gl-section-divider-right"></div>
                </div>
                <div class="gl-tile-grid">
                    <div class="gl-tile" data-prop="excel-bhimtal" data-cat="property" data-title="Excel Hotels, Bhimtal" data-caption="Excel Hotels &amp; Resorts, Bhimtal">
                        <img src="assets/img/Bhimtal.webp" alt="Excel Bhimtal" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Excel Hotels, Bhimtal</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="excel-bhimtal" data-cat="property" data-title="Bhimtal Gallery" data-caption="Excel Hotels Bhimtal – Gallery">
                        <img src="assets/img/Excel-Bhimtal-gallery1.png" alt="Bhimtal Gallery" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Bhimtal Gallery</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="excel-bhimtal" data-cat="property" data-title="Bhimtal Gallery" data-caption="Excel Hotels Bhimtal – Gallery">
                        <img src="assets/img/Excel-Bhimtal-gallery2.png" alt="Bhimtal Gallery" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Bhimtal Gallery</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile featured" data-prop="excel-bhimtal" data-cat="experiences" data-title="Bhimtal Pool" data-caption="Excel Hotels Bhimtal – Swimming Pool">
                        <img src="assets/img/Bhimtal-Pool.png" alt="Bhimtal Pool" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Swimming Pool</h6><span>Experiences</span></div></div>
                    </div>
                    <div class="gl-tile-stack">
                        <div class="gl-tile" data-prop="excel-bhimtal" data-cat="rooms" data-title="Bhimtal Rooms" data-caption="Excel Hotels Bhimtal – Rooms">
                            <img src="assets/img/Bhimtal-rooms1.jpg" alt="Bhimtal Rooms" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Bhimtal Rooms</h6><span>Rooms &amp; Suites</span></div></div>
                        </div>
                        <div class="gl-tile" data-prop="excel-bhimtal" data-cat="rooms" data-title="Premium Rooms" data-caption="Excel Hotels Bhimtal – Premium Rooms">
                            <img src="assets/img/Bhimtal-rooms2.jpg" alt="Bhimtal Premium" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Premium Rooms</h6><span>Rooms &amp; Suites</span></div></div>
                        </div>
                    </div>
                    <div class="gl-tile" data-prop="excel-bhimtal" data-cat="property" data-title="Bhimtal Gallery" data-caption="Excel Hotels Bhimtal – Gallery">
                        <img src="assets/img/Excel-Bhimtal-gallery3.png" alt="Bhimtal Gallery" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Bhimtal Gallery</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="excel-bhimtal" data-cat="events" data-title="Bhimtal Events" data-caption="Excel Hotels Bhimtal – Events">
                        <img src="assets/img/Excel-Bhimtal-gallery4.png" alt="Bhimtal Events" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Bhimtal Events</h6><span>Events</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="excel-bhimtal" data-cat="property" data-title="Bhimtal Gallery" data-caption="Excel Hotels Bhimtal – Gallery">
                        <img src="assets/img/Excel-Bhimtal-gallery5.png" alt="Bhimtal Gallery" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Bhimtal Gallery</h6><span>Property</span></div></div>
                    </div>
                </div>
            </div>

            <!-- ===== MANGOBLOOM RIVER RESORT ===== -->
            <div class="gl-prop-section" data-section="mangobloom">
                <div class="gl-section-header">
                    <div class="gl-section-divider"></div>
                    <span class="gl-section-title">Mangobloom River Resort, Jim Corbett</span>
                    <div class="gl-section-divider-right"></div>
                </div>
                <div class="gl-tile-grid">
                    <div class="gl-tile" data-prop="mangobloom" data-cat="property" data-title="Mangobloom River Resort" data-caption="Mangobloom River Resort, Jim Corbett">
                        <img src="assets/img/egallery6.jpg" alt="Mangobloom Resort" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Mangobloom River Resort</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="mangobloom" data-cat="property" data-title="Mangobloom Gallery" data-caption="Mangobloom River Resort – Gallery">
                        <img src="assets/img/egallery7.jpg" alt="Mangobloom Gallery" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Mangobloom Gallery</h6><span>Property</span></div></div>
                    </div>
                    <div class="gl-tile" data-prop="mangobloom" data-cat="rooms" data-title="Mangobloom Rooms" data-caption="Mangobloom River Resort – Rooms">
                        <img src="assets/img/egallery8.jpg" alt="Mangobloom Rooms" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Mangobloom Rooms</h6><span>Rooms &amp; Suites</span></div></div>
                    </div>
                    <div class="gl-tile featured" data-prop="mangobloom" data-cat="experiences" data-title="Mangobloom Experiences" data-caption="Mangobloom River Resort – Experiences">
                        <img src="assets/img/egallery9.jpg" alt="Mangobloom Experiences" loading="lazy">
                        <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Mangobloom Experiences</h6><span>Experiences</span></div></div>
                    </div>
                    <div class="gl-tile-stack">
                        <div class="gl-tile" data-prop="mangobloom" data-cat="dining" data-title="Mangobloom Dining" data-caption="Mangobloom River Resort – Dining">
                            <img src="assets/img/egallery10.jpg" alt="Mangobloom Dining" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Mangobloom Dining</h6><span>Dining</span></div></div>
                        </div>
                        <div class="gl-tile" data-prop="mangobloom" data-cat="property" data-title="Mangobloom Gallery" data-caption="Mangobloom River Resort">
                            <img src="assets/img/egallery11.jpg" alt="Mangobloom Gallery" loading="lazy">
                            <div class="gl-tile-overlay"><div class="gl-tile-label"><h6>Mangobloom Resort</h6><span>Property</span></div></div>
                        </div>
                    </div>
                </div>
            </div>

        </section>
    </main>

    <!-- ======= Fullscreen Lightbox ======= -->
    <div class="gl-lightbox" id="glLightbox" role="dialog" aria-modal="true" aria-label="Image viewer">
        <button class="gl-lb-close" id="glLbClose" aria-label="Close">&#215;</button>
        <div class="gl-lb-img-wrap" id="glLbImgWrap">
            <img id="glLbImg" src="" alt="" draggable="false">
            <button class="gl-lb-arrow left" id="glLbPrev" aria-label="Previous"><i class="bi bi-chevron-left"></i></button>
            <button class="gl-lb-arrow right" id="glLbNext" aria-label="Next"><i class="bi bi-chevron-right"></i></button>
        </div>
        <div class="gl-lb-caption" id="glLbCaption"></div>
        <div class="gl-lb-counter" id="glLbCounter"></div>
    </div>

    <!-- ======= Footer ======= -->
    <footer id=footer><div class=footer-top><div class=container><div class=row><div class=col-md-4><div class=footer-info><img alt class=img-fluid decoding=async fetchpriority=high src=assets/img/excel-logo.webp></div></div><div class=col-md-4><div class=quicklinks><h6>QUICK LINKS</h6><ul><li><a class="font-Brandon color-dgrey" href=aboutus1.html>About us</a><li><a class="font-Brandon color-dgrey" href=contact.html>Contact us</a><li><a class="font-Brandon color-dgrey" href=gallery.html>Gallery</a><li><a class="font-Brandon color-dgrey" href=petpolicy1.html>Pet Policy</a></ul></div></div><div class=col-md-4><div class=quicklinks><h6>CONTACT US</h6><p class=m-0><a class="font-Brandon color-dgrey f-s-16" href=tel:+919211301999>+91 9211301999</a><p class=m-0><a class="font-Brandon color-dgrey f-s-16" href=Address>The Iconic Corenthum, Office No : 805 B , 8th Floor , Iconic Tower, Plot No A-41, Sector 62, Noida, Uttar Pradesh 201309</a><p class=m-0><a class="font-Brandon color-dgrey f-s-16" href=mailto:resv@excelhotelandresort.com>resv@excelhotelandresort.com</a></div></div></div></div></div></footer>

    <!-- Vendor JS -->
    <script src="assets/vendor/aos/aos.js"></script>
    <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
    <script src="assets/js/main.min.js"></script>

    <!-- ======= Gallery Controller ======= -->
    <script>
    (function () {
        'use strict';

        var allTiles   = [];
        var lbImages   = [];
        var lbIndex    = 0;
        var activeProp = 'all';
        var activeCat  = 'all';

        function init() {
            // Collect all tiles (direct + inside stacks)
            allTiles = Array.prototype.slice.call(document.querySelectorAll('.gl-tile[data-prop]'));

            // Attach lightbox click to each tile
            allTiles.forEach(function (tile, i) {
                tile.addEventListener('click', function () { openLightbox(i); });
                tile.setAttribute('tabindex', '0');
                tile.setAttribute('role', 'button');
                tile.addEventListener('keydown', function (e) {
                    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openLightbox(i); }
                });
            });

            // Property filter
            document.querySelectorAll('.gl-prop-btn').forEach(function (btn) {
                btn.addEventListener('click', function () {
                    document.querySelectorAll('.gl-prop-btn').forEach(function (b) {
                        b.classList.remove('active'); b.setAttribute('aria-selected','false');
                    });
                    btn.classList.add('active'); btn.setAttribute('aria-selected','true');
                    activeProp = btn.dataset.prop;
                    applyFilters();
                });
            });

            // Category filter
            document.querySelectorAll('.gl-cat-btn').forEach(function (btn) {
                btn.addEventListener('click', function () {
                    document.querySelectorAll('.gl-cat-btn').forEach(function (b) { b.classList.remove('active'); });
                    btn.classList.add('active');
                    activeCat = btn.dataset.cat;
                    applyFilters();
                });
            });

            // Lightbox controls
            document.getElementById('glLbClose').addEventListener('click', closeLightbox);
            document.getElementById('glLbPrev').addEventListener('click', function () { nav(-1); });
            document.getElementById('glLbNext').addEventListener('click', function () { nav(1); });
            document.getElementById('glLightbox').addEventListener('click', function (e) {
                if (e.target === this) closeLightbox();
            });
            document.addEventListener('keydown', function (e) {
                var lb = document.getElementById('glLightbox');
                if (!lb.classList.contains('open')) return;
                if (e.key === 'ArrowLeft')  nav(-1);
                if (e.key === 'ArrowRight') nav(1);
                if (e.key === 'Escape')     closeLightbox();
            });

            // Swipe
            var sx = 0;
            var lb = document.getElementById('glLightbox');
            lb.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, { passive: true });
            lb.addEventListener('touchend',   function (e) {
                var dx = e.changedTouches[0].clientX - sx;
                if (Math.abs(dx) > 50) nav(dx < 0 ? 1 : -1);
            }, { passive: true });

            applyFilters();
        }

        function applyFilters() {
            lbImages = [];
            var sections = document.querySelectorAll('.gl-prop-section');

            sections.forEach(function (sec) {
                var secProp = sec.dataset.section;
                var propMatch = activeProp === 'all' || secProp === activeProp;

                // Show/hide entire section based on property filter
                if (!propMatch) {
                    sec.classList.add('hidden');
                    return;
                }
                sec.classList.remove('hidden');

                // Filter individual tiles by category
                var tiles = sec.querySelectorAll('.gl-tile[data-prop]');
                tiles.forEach(function (tile) {
                    var catMatch = activeCat === 'all' || tile.dataset.cat === activeCat;
                    if (catMatch) {
                        tile.classList.remove('hidden');
                        lbImages.push(tile);
                    } else {
                        tile.classList.add('hidden');
                    }
                });

                // Hide stacks if all their children are hidden
                sec.querySelectorAll('.gl-tile-stack').forEach(function (stack) {
                    var visible = stack.querySelectorAll('.gl-tile:not(.hidden)');
                    stack.style.display = visible.length ? '' : 'none';
                });

                // Hide section if all tiles hidden after category filter
                var visibleInSec = sec.querySelectorAll('.gl-tile[data-prop]:not(.hidden)');
                sec.classList.toggle('hidden', visibleInSec.length === 0);
            });

            var countEl = document.getElementById('glCount');
            if (countEl) countEl.textContent = lbImages.length + (lbImages.length === 1 ? ' Photo' : ' Photos');

            var empty = document.getElementById('glEmpty');
            if (empty) empty.classList.toggle('visible', lbImages.length === 0);
        }

        function openLightbox(tileIndex) {
            var tile = allTiles[tileIndex];
            var pos  = lbImages.indexOf(tile);
            lbIndex  = pos >= 0 ? pos : 0;
            renderLb();
            document.getElementById('glLightbox').classList.add('open');
            document.body.style.overflow = 'hidden';
        }

        function closeLightbox() {
            document.getElementById('glLightbox').classList.remove('open');
            document.body.style.overflow = '';
        }

        function nav(dir) {
            if (!lbImages.length) return;
            lbIndex = (lbIndex + dir + lbImages.length) % lbImages.length;
            renderLb();
        }

        function renderLb() {
            var tile  = lbImages[lbIndex];
            if (!tile) return;
            var img   = document.getElementById('glLbImg');
            var wrap  = document.getElementById('glLbImgWrap');
            var cap   = document.getElementById('glLbCaption');
            var cnt   = document.getElementById('glLbCounter');
            wrap.classList.add('loading');
            img.onload = function () { wrap.classList.remove('loading'); };
            img.src = tile.querySelector('img').src;
            img.alt = tile.dataset.title || '';
            cap.textContent = tile.dataset.caption || tile.dataset.title || '';
            cnt.textContent = (lbIndex + 1) + ' / ' + lbImages.length;
        }

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', init);
        } else {
            init();
        }
    })();
    </script>

</body>
</html>
'''

with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where main starts and cut everything from there
idx = content.find(HERO_END_MARKER)
if idx == -1:
    print("ERROR: Could not find main marker")
else:
    new_content = content[:idx] + NEW_MAIN
    with open('gallery.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Done! File size: {len(new_content)} chars")
    print(f"Section headers: {new_content.count('gl-section-header')}")
    print(f"Tiles: {new_content.count('class=\"gl-tile\"') + new_content.count('class=\"gl-tile featured\"')}")
    print(f"Featured tiles: {new_content.count('class=\"gl-tile featured\"')}")
    print(f"Stacked groups: {new_content.count('class=\"gl-tile-stack\"')}")
