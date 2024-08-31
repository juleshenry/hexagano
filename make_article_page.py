
def make_article_page(headline, article):
    page = """
    import Link from "next/link";
    import styles from "../../catalog.module.css";

    export default function MakePage() {
    return (
        <>
        <div className={styles.pagestyle}>
            <div>
        """
    page += f"""
            <h2>{headline}</h2>
                <div>{article}</div>
                """
    page += """
            <div>
            Back to <Link href="/">Home</Link>
            </div>
        </div>
        </>
    );
    }
    """
    return article