
def make_article_page(headline, article):
    # fmt: off
    page = \
"""import Link from "next/link";
import styles from "../../catalog.module.css";

export default function MakePage() {
return (
    <>
    <div className={styles.pagestyle}>
        <div>
        """
    page += f"""
        <h2>{headline}</h2>
            <div className={{styles.article}}>{article}</div>
                """
    page += """
        <div>
        Back to <Link href="/">Home</Link>
        </div>
        </div>
    </div>
    </>
);
}
    """
    # fmt: on
    return page


if __name__=='__main__':
    article = "A body Another body Yet another body "*5
    headline = "A headline"
    print(make_article_page(headline=headline, article=article))