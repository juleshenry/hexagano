
    import Link from "next/link";
    import Head from "next/head";
    import styles from "./index.module.css";
    
    const Home = () => {
    
      return (
        <div>
          <Head>
            <link rel="icon" href="public/favicon.ico" />
          </Head>
          <div className={styles.topBar}></div>
          <div className={styles.pagestyle}>
            <Link className={styles.brandLogo} href="/">
              ONE WORLD GAZETTE
            </Link>
            <div className={styles.newsFeed}>          
              <hr className={styles.separator} />
              <Link className={styles.titular} href="/e1/ASIO-boss-caught-in-political-crossfire-over-Gaza-refugees-High-profile">ASIO-boss-caught-in-political-crossfire-over-Gaza-refugees-High-profile</Link>
              
              <hr className={styles.separator} />
              <Link className={styles.titular} href="/e1/Brazilian-Judge-Orders-Total-Suspension-of-Elon-Musks-X-Social">Brazilian-Judge-Orders-Total-Suspension-of-Elon-Musks-X-Social</Link>
              
              <hr className={styles.separator} />
              <Link className={styles.titular} href="/e1/Church-roof-collapses-in-Brazil-city-killing-at-least-two">Church-roof-collapses-in-Brazil-city-killing-at-least-two</Link>
              
              <hr className={styles.separator} />
              <Link className={styles.titular} href="/e1/Irans-president-says-his-country-needs-more-than-$100-billion">Irans-president-says-his-country-needs-more-than-$100-billion</Link>
              
              <hr className={styles.separator} />
              <Link className={styles.titular} href="/e1/Israeli-strikes-kill-48-in-Gaza;-polio-vaccinations-to-begin">Israeli-strikes-kill-48-in-Gaza;-polio-vaccinations-to-begin</Link>
              
              <hr className={styles.separator} />
              <Link className={styles.titular} href="/e1/Rest-of-the-list">Rest-of-the-list</Link>
              
              <hr className={styles.separator} />
              <Link className={styles.titular} href="/e1/Serbia-unlikely-to-join-EU-before-end-of-decade-says">Serbia-unlikely-to-join-EU-before-end-of-decade-says</Link>
              
              <hr className={styles.separator} />
              <Link className={styles.titular} href="/e1/The-Russian-Navy-Might-Be-Making-a-Comeback-Significant-update">The-Russian-Navy-Might-Be-Making-a-Comeback-Significant-update</Link>
              
              <hr className={styles.separator} />
              <Link className={styles.titular} href="/e1/Zionist-aggression-death-toll-in-Gaza-Strip-tops-40691-martyrs">Zionist-aggression-death-toll-in-Gaza-Strip-tops-40691-martyrs</Link>
              <hr className={styles.separator} />

            </div>
            <Link className={styles.bigButton} href="/catalog">
              🌐
            </Link>
          </div>
        </div>
      );
    };
    
    export default Home;
    